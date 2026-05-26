import os
import streamlit as st
import time
import joblib
import pandas as pd

# Configuración inicial de la página
st.set_page_config(page_title="Módulo de auditoría de fraude - IA", page_icon="⚠️", layout="wide")

#definimos una función para cargar el modelo una sola vez y guardar en caché para mejorar el rendimiento
@st.cache_resource
def cargar_modelo():
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    modelo = joblib.load(os.path.join(ruta_actual, "..", "models", "modelo_fraude_rf.pkl"))
    scaler = joblib.load(os.path.join(ruta_actual, "..", "models", "scaler_robusto.pkl"))
    return modelo, scaler

modelo, scaler = cargar_modelo()

#encabezado del panel de control
st.title("Sistema de Monitoreo de Fraude Financiero")
st.subheader("Consola de Auditoría Avanzada para Analistas de Riesgo")
st.write("Introduzca las métricas de la transacción bajo revisión para consultar el dictamen del clasificador de IA.")

st.markdown("---")

# creamos dos columnas principales en la pantalla: izquierda para datos, derecha para resultados
col_izquierda, col_derecha = st.columns([1, 1])

with col_izquierda:
    st.write("### Parámetros de la Transacción Entrante")
    
    with st.form("formulario_analista"):
        #variables físicas directas
        cantidad = st.number_input("Monto Evaluado (Amount en Pesos)", min_value=1000.00, value=50000.0, step=1000.0)
        
        st.write("**Variables de Comportamiento (Mapeo a Componentes Principales)**")
        # Simulamos escenarios que un analista investigaría
        perfil_comercio = st.selectbox(
                "Patrón de Comercio", 
                ["Normal (Supermercados/Servicios)", "De Alto Riesgo (Casino/Cripto/Retiros)", "Electrónica Nocturna"]
            )
        consistencia_IP = st.selectbox(
                "Geolocalización / IP del Dispositivo", 
                ["IP Habitual (Mismo rango)", "IP Sospechosa (Cambio drástico de ubicación)", "Uso de VPN/Proxy"]
            )
        alertas_previas = st.slider("Alertas de seguridad previas en las últimas 24hs", 0, 5, 0)
            
        boton_auditar = st.form_submit_button("Ejecutar Análisis de Riesgo")


# 4. LÓGICA DE PROCESAMIENTO (Tras bambalinas)
if boton_auditar:
    # Inicializamos las 28 variables PCA en 0.0 (punto neutral del PCA)
    componentes_pca = {f"V{i}": 0.0 for i in range(1, 29)}
    
    # El analista altera los componentes clave (V1, V14, V17 suelen ser los más correlacionados)
    if perfil_comercio == "De Alto Riesgo (Casino/Cripto/Retiros)":
        componentes_pca["V1"] = -5.4
        componentes_pca["V3"] = -3.8
    elif perfil_comercio == "Electrónica Nocturna":
        componentes_pca["V1"] = -2.1
        
    if consistencia_IP == "IP Sospechosa (Cambio drástico de ubicación)":
        componentes_pca["V2"] = -4.2
        componentes_pca["V4"] = 2.9
    elif consistencia_IP == "Uso de VPN/Proxy":
        componentes_pca["V2"] = -6.1
        componentes_pca["V11"] = 4.0
        
    if alertas_previas > 1:
        componentes_pca["V14"] = -4.8  # Componente crítico de anomalía
        componentes_pca["V17"] = -5.1

    #transformamos la cantidad en pesos a euros de 2013
    euros_actuales = cantidad / 1640
    #ipc euro actual 2,2% - IPC euro 2013 1,1% = 1,1% de aumento
    factor_deflacion= 1.1/2.2
    monto_equivalente_sep2013= euros_actuales * factor_deflacion

    # Escalamos los componentes con el scaler robusto (simulando la transformación que se hizo en el entrenamiento)
    cantidad_escalada = scaler.transform([[monto_equivalente_sep2013]])[0][0]

    # Agregamos Tiempo y Cantidad
    componentes_pca["Amount"] = cantidad_escalada
    componentes_pca["Time"] = time.time() % 86400
    
    # Armamos el DataFrame con el orden exacto que espera tu archivo .pkl
    columnas_ordenadas =["Time"] + [f"V{i}" for i in range(1, 29)] + ["Amount"]
    df_analisis = pd.DataFrame([componentes_pca])[columnas_ordenadas]
    
    # Predecimos la probabilidad con el modelo
    probabilidad_fraude = modelo.predict_proba(df_analisis)[0, 1]

    # Mostramos los resultados en la columna de la derecha
    with col_derecha:
        st.write("### 📊 Dictamen y Diagnóstico del Modelo")
        
        # Formateo estético del veredicto
        if probabilidad_fraude < 0.20:
            st.success(f"### Transacción Aprobada (Riesgo Bajo)")
            nivel = "SEGURO"
            color_metrica = "normal"
        elif 0.20 <= probabilidad_fraude < 0.60:
            st.warning(f"### Transacción Retenida (Riesgo Moderado)")
            nivel = "REVISIÓN MANUAL"
            color_metrica = "off"
        else:
            st.error(f"### Transacción Bloqueada (Riesgo Crítico)")
            nivel = "FRAUDE DETECTADO"
            color_metrica = "inverse"
            
        # Métricas principales en tarjetas visuales
        st.metric(label="Veredicto de la IA", value=nivel)
        st.metric(label="Score de Probabilidad de Fraude", value=f"{probabilidad_fraude*100:.2f} %")
        
        st.write("---")
        st.write("**Matriz de Componentes Enviada al Modelo (Vector Input):**")
        
        # Mostramos los componentes que modificó el analista para que vea los datos que entraron al PCA
        componentes_interesantes = {k: v for k, v in componentes_pca.items() if v != 0.0 or k in ["Amount", "Time"]}
        df_visual = pd.DataFrame(componentes_interesantes.items(), columns=["Componente / Variable", "Valor Numérico"])
        
        # Muestra una tablita interactiva dentro de la app
        st.dataframe(df_visual, use_container_width=True)
else:
    with col_derecha:
        st.info("A la espera de parámetros. Modifique los datos de la izquierda y haga clic en 'Ejecutar Análisis de Riesgo' para calcular el diagnóstico.")