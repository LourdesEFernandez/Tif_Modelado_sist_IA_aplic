_Este archivo está destinado a documentar todo el proceso de desarrollo del TIF. 
Una vez que se defina el tema y problema a resolver se volcaran a este archivo._

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
