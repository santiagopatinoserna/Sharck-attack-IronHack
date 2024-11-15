# Análisis de Datos de Ataques de Tiburones

## Proyecto de Análisis de Datos - Ironhack Bootcamp

Este repositorio contiene el análisis de datos realizado para una empresa de seguros interesada en optimizar su oferta de seguros para actividades acuáticas en zonas con mayor incidencia de ataques de tiburones· Nuestro objetivo fue analizar y extraer insights de los datos para identificar los lugares y épocas del año más propensos a estos incidentes y proponer recomendaciones sobre dónde y cuándo implementar seguros·

## Objetivo del Proyecto

El análisis de datos de ataques de tiburones fue realizado para ayudar a la empresa de seguros a:

- Identificar los países con mayor número de ataques de tiburones en actividades acuáticas·
- Determinar las épocas del año con más incidencias, enfocándonos en los meses con mayor probabilidad de ataque·
- Evaluar la gravedad de los ataques (fatales o no fatales) para definir el tipo de seguro adecuado·

Nuestro análisis permite a la aseguradora dirigir sus esfuerzos de publicidad y desarrollo de productos de manera más efectiva·

## Herramientas Utilizadas

Para el desarrollo y análisis de este proyecto, utilizamos las siguientes herramientas y bibliotecas:

- **Python**: Herramienta principal para el procesamiento y análisis de datos·
- **Pandas**: Para la limpieza, transformación y manipulación de los datos·
- **Fuzzywuzzy**: Para la correspondencia y estandarización de nombres de países y otros datos textuales·
- **Matplotlib y Seaborn**: Para la visualización de datos y generación de gráficos que ilustran los hallazgos·
- **Regex (re)**: Para limpiar y formatear datos de fecha·
- **Visual Studio Code y GitHub**: Como entornos de desarrollo y para la colaboración en el proyecto·

## Proceso de Limpieza de Datos

Durante el análisis, nos enfrentamos al reto de limpiar y estructurar el conjunto de datos de ataques de tiburones para obtener información precisa· Algunos de los pasos realizados fueron:

- **Eliminación de columnas irrelevantes** para el análisis·
- **Formato de datos**: Estandarización de nombres de países y lugares, y conversión de fechas al formato `datetime`·
- **Limpieza de nulos**: Eliminación de filas con valores nulos en columnas clave, y uso de técnicas como el `backfill` para completar datos faltantes en fechas ordenadas·
- **Separación de fechas**: Extracción de mes y año a partir de la columna de fecha corregida·

Estas técnicas aseguraron un conjunto de datos limpio y estructurado, esencial para un análisis fiable·

## Conclusiones del Análisis

Al final del análisis, obtuvimos los siguientes hallazgos clave:

1· **Ubicaciones con Mayor Incidencia**: Los países con mayor número de ataques registrados fueron Estados Unidos, Sudáfrica y Australia, lo cual los convierte en mercados prioritarios para la venta de seguros·
2· **Estacionalidad de los Ataques**: Los ataques se concentran en los meses de verano (particularmente entre junio y septiembre en el hemisferio norte)· Recomendamos un esfuerzo de marketing intensivo en estos meses y en los previos·
3· **Gravedad de los Ataques**: La mayoría de los ataques no son fatales· Por lo tanto, una póliza general para accidentes de bajo riesgo sería suficiente y atractiva para los turistas y residentes de estas áreas·

### Recomendaciones de Seguro

Basándonos en el análisis, recomendamos a la empresa de seguros:

- **Focalizar las campañas** en Estados Unidos, Sudáfrica y Australia·
- **Implementar una póliza general para accidentes no fatales** que cubra actividades acuáticas en las áreas identificadas como de mayor riesgo·
- **Aumentar la publicidad en los meses de primavera y principios de verano** para captar la atención de los turistas y locales que planean realizar actividades acuáticas·

## Entregables

- **Código**: El código del proyecto, incluyendo scripts de limpieza y análisis de datos, se encuentra en este repositorio·
- **Visualizaciones**: Los gráficos y visualizaciones generados para ilustrar los hallazgos·
- **Informe**: Un documento con el resumen de los hallazgos y recomendaciones·

## Enlaces

- [Dataset utilizado](Link al Dataset)
- [Documentación del proyecto](Link a la documentación)
- [Presentación del proyecto](Link a la presentación)

## Participantes

- Esteban Cristos Muzzupappa - [LinkedIn](https://www·linkedin·com/in/esteban-cristos-muzzupappa/)
- Gerardo Jimenez - [LinkedIn](https://www·linkedin·com/in/gerardo-jimenez/) 
