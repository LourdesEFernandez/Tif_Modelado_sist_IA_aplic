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



## Ciclo técnico
---
## Resumen visual del contenido de este repositorio
|    Carpeta	    | Contenido clave                       |
| :---              | :---                                  |
| **data/**	        | **raw/** : Dataset original.          |
|                   | **processed/** : Los datos limpios, transformados y listos para entrenar el modelo. |
| **docs/**         |	Documentación teórica y técnica del proyecto (manual de usuario).  |
| **models/**       |	El modelo de IA guardado (.pkl). |
| **notebooks/**    |	Archivos de EDA, visualizaciones y pruebas de diferentes algoritmos de IA (.ipynb). |
| **src/**          |	Scripts de Python que ejecutan el sistema automáticamente. |
| **requirements.txt** |	La lista de librerías necesarias y sus versiones. |


## Instrucciones de instalación
_Pasos a seguir para correr la app localmente_

## Equipo de trabajo
* Barboza, María Eugenia
* Fernández, Lourdes Eliana
* Laime, Diego Eduardo
* Rios Tejerina, Antonella Melisa
