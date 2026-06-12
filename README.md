# SISTEMA DE DETECCIÓN DE FRAUDE
## Descripción del problema
Las entidades financieras procesan grandes  volumenes de transacciones electrónicas diariamente. Dentro de este volumen masivo, una pequeña proporción corresponde a operaciones fraudulentas, las cuales generan pérdidas económicas significativas y afectan la confianza de los clientes.
El problema consiste en identificar transacciones fraudulentas , que permitan a  entidades bancarias bloquear dichas operaciones evitando potenciales perdidas a partir de datos históricos de operaciones.

## Solución:
Desarrollar un sistema basado en Machine Learning supervisado, que aprenda a partir de datos históricos etiquetados, detecte la mayor cantidad posible de fraudes (alto recall), minimice falsos positivos (precision razonable) y sea escalable y aplicable en entornos reales.

**La IA nos permite:**
* Aprender patrones complejos automáticamente.
* Manejar grandes volúmenes de datos.
* Detección de patrones oculto.
* Adaptabilidad
* Que los modelos puedan reentrenarse con nuevos datos.
* Adaptarse a nuevos tipos de fraude.
* Estimar la probabilidad de fraude, lo que permite: ajustar umbrales
* Diseñar estrategias de negocio (alerta, bloqueo, revisión).

## ¿Cómo lo hicimos? (Detrás de escena)
El desarrollo del proyecto se dividió en dos grandes etapas:

- El "Cerebro" (El Modelo de IA):

    Tomamos un conjunto de datos con miles de transacciones históricas (algunas reales y muchas de prueba).

    Analizamos el comportamiento de los datos: montos, horarios y patrones típicos de los estafadores.

    Entrenamos a un algoritmo de Inteligencia Artificial para que "aprendiera" a diferenciar una operación normal de una sospechosa. Nos aseguramos de que el sistema sea muy preciso para no dar falsas alarmas, pero tampoco dejar pasar ningún engaño.

- La "Cara Visible" (La Aplicación Web):

    Como los modelos matemáticos se ejecutan en código y son difíciles de usar para alguien que no programa, construimos una aplicación web interactiva utilizando Streamlit.

    Esta plataforma conecta de forma transparente nuestro "cerebro" de IA con una interfaz visual amigable, con botones, formularios y gráficos interactivos.

## ¿Para quién está destinado?
Esta aplicación está pensada principalmente para:

- Analistas de Fraude y Equipos de Seguridad: Quienes necesitan una herramienta rápida y visual para auditar transacciones sospechosas sin tener que escribir código.

- Pequeñas y Medianas Empresas (PyMEs) o Fintechs: Negocios que manejan pagos digitales y buscan una solución accesible para proteger sus operaciones y a sus clientes.

- Auditores y Administradores: Usuarios que necesitan subir un listado de movimientos del día y obtener un reporte automático con las alertas de riesgo más altas.

## Flujo de Operación en la Práctica (Workflow del Analista)
La aplicación está optimizada para integrarse al flujo de trabajo diario de un equipo de mitigación de riesgos:

Auditoría y Scoring Individual: El analista puede ingresar las variables específicas de una transacción bajo sospecha (montos, flags de comportamiento, datos de origen/destino) para obtener un score de riesgo inmediato y el dictamen del modelo (Legítima o Potencial Fraude). Esto facilita la toma de decisiones rápidas ante alertas aisladas.

## Dataset 
El conjunto de datos con el que vamos a trabajar se obtuvo de la plataforma de [_kaggle_](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data) 

_**Descripción:**_

El conjunto de datos contiene transacciones realizadas por tarjetas de crédito en septiembre de 2013 por titulares de tarjetas europeas.
Este conjunto de datos presenta transacciones que ocurrieron en dos días, donde tenemos 492 fraudes de 284.807 transacciones. El mismo está muy desequilibrado, la clase positiva (fraudes) representa el 0.172% de todas las transacciones.
Contiene solo variables de entrada numéricas que son el resultado de una transformación de PCA. Desafortunadamente, debido a problemas de confidencialidad, no se pueden proporcionar las características originales y más información de antecedentes sobre los datos.

| Cant. Registros | Cant. Variables | Variable Objetivo |
| --------------- | --------------- | ----------------- |
| 284.807         | 31              | Class             |
---
| Variable            | Tipo     | Detalle                                   |
| :---                | :---     | :---                                      |
| **V1, V2, ... V28** | Numérica | componentes principales obtenidos con PCA |
| **Tiempo**          | Numérica | contiene los segundos transcurridos entre cada transacción y la primera transacción en el conjunto de datos |
| **Cantidad**        | Numérica | es la cantidad de la transacción          |
| **Class**           | Numérica | 0 = normal ; 1 = fraude                   |


## Resumen visual del contenido de este repositorio
|    Carpeta	    | Contenido clave                       |
| :---              | :---                                  |
| **docs/**         |	Documentación teórica y técnica del proyecto (manual de usuario).  |
| **models/**       |	El modelo de IA guardado (.pkl), escalador usado (.pkl) |
| **notebooks/**    |	Archivos de EDA, visualizaciones y pruebas de diferentes algoritmos de IA (.ipynb). |
| **src/**          |	Scripts de Python con la app |
| **requirements.txt** |	La lista de librerías necesarias y sus versiones. |


## Instrucciones de instalación
- **Paso 1:** Descargar carpeta de archivos.zip desde el boton ``` <> Code ```
- **Paso 2:** Descomprimir archivo en una ubicación cómoda por ej: 
    
    ``` C:/Documentos/carpeta_proyecto ```

- **Paso 3:** Crear entorno virtual en su PC (solo la primera vez)
    
    Desde tu terminal ejecuta el siguiente comando:
    
  ``` python -m venv src/.venv ```

- **Paso 4:** Instalar librerias usando el archivo de texto requirements.txt

    Comando:    ``` src/.venv\Scripts\pip install -r src/requirements.txt ```

- **Paso 5:** Ahora puedes correr la app desde la carpeta con los archivos clickeando en 
``` correr_sistema_fraude.bat ```

## Equipo de trabajo
* Barboza, María Eugenia
* Fernández, Lourdes Eliana
* Laime, Diego Eduardo
* Rios Tejerina, Antonella Melisa
