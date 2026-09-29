# TripleTenModule7
TripleTen Module 7

## Análisis Exploratorio y Aplicación Web de Vehículos

Descripción del proyecto

Este proyecto corresponde al Proyecto 7, cuyo objetivo es realizar un análisis exploratorio de un conjunto de datos de anuncios de vehículos y desarrollar una aplicación web interactiva que permita visualizar y explorar algunas de las características más relevantes de los vehículos publicados.

El proyecto integra dos componentes principales:

Análisis exploratorio de datos (EDA) mediante un Jupyter Notebook.

Aplicación web interactiva desarrollada con Streamlit y desplegada en Render.

La aplicación permite visualizar gráficamente la información contenida en el conjunto de datos, utilizando elementos interactivos para facilitar la exploración de los datos.

## Aplicación desplegada

La aplicación está disponible públicamente en Render:

🔗 https://tripletenmodule7.onrender.com

Puedes acceder directamente desde cualquier navegador para explorar las visualizaciones y funcionalidades desarrolladas en el proyecto.

## Objetivos

Los principales objetivos del proyecto son:

- Explorar y comprender las características del conjunto de datos de vehículos.

- Identificar patrones y relaciones entre diferentes variables.

- Analizar visualmente la distribución de determinadas características.

- Construir visualizaciones interactivas mediante Python.

- Desarrollar una aplicación web utilizando Streamlit.

- Desplegar la aplicación en Render.

- Aplicar buenas prácticas de organización y documentación de un proyecto de Ciencia de Datos.

## Aplicación web

La aplicación contiene elementos interactivos y visualizaciones que permiten explorar los datos de forma sencilla.

Entre los componentes principales se encuentran:

- Encabezados y secciones descriptivas para facilitar la navegación.

- Histograma, utilizado para analizar la distribución de una variable.

- Gráfico de dispersión, utilizado para estudiar la relación entre variables.

- Elementos interactivos, como botones o casillas de verificación, que permiten controlar la visualización de los datos.

- La aplicación fue desarrollada con Streamlit, lo que permite transformar el análisis realizado en Python en una interfaz web interactiva.

## Estructura del repositorio

El repositorio está organizado de la siguiente manera:

.
├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
└── EDA.ipynb

## Descripción de los archivos

## Archivo	Descripción
- README.md	Documentación del proyecto, instrucciones de instalación, ejecución y enlace a la aplicación desplegada.
- app.py	Código fuente de la aplicación web desarrollada con Streamlit.
- vehicles_us.csv	Conjunto de datos utilizado para realizar el análisis y generar las visualizaciones.
- requirements.txt	Lista de dependencias necesarias para ejecutar el proyecto.
- EDA.ipynb	Jupyter Notebook que contiene el análisis exploratorio de los datos.

Esta estructura permite separar claramente la documentación, los datos, el análisis exploratorio y el código de la aplicación.

## Análisis exploratorio de datos

El análisis exploratorio se encuentra en:

EDA.ipynb


En este notebook se realiza una exploración inicial del conjunto de datos con el propósito de comprender:

- La estructura de los datos.

- Los tipos de variables.

- Los valores ausentes.

- Las estadísticas descriptivas.

- La distribución de las principales variables.

- Las posibles relaciones entre características de los vehículos.

- Los patrones que pueden ser representados mediante visualizaciones.

- El EDA sirve como base para seleccionar las variables y visualizaciones utilizadas posteriormente en la aplicación web.

# Datos

El proyecto utiliza el archivo:

- vehicles_us.csv


Este archivo contiene los datos de los anuncios de vehículos utilizados tanto para el análisis exploratorio como para la aplicación web.

La aplicación carga este archivo para generar las visualizaciones que se presentan al usuario.

<b>Nota:</b> El archivo de datos debe encontrarse en el directorio raíz del proyecto para que la aplicación pueda localizarlo correctamente cuando se ejecuta localmente o se despliega en Render.

## Tecnologías utilizadas

El proyecto fue desarrollado utilizando las siguientes herramientas:

Python — lenguaje principal de programación.

Pandas — manipulación y análisis de datos.

Plotly — generación de visualizaciones interactivas.

Streamlit — desarrollo de la aplicación web.

Jupyter Notebook — desarrollo del análisis exploratorio.

Render — despliegue de la aplicación web.

Git / GitHub — control de versiones y almacenamiento del proyecto.

Las versiones y dependencias específicas utilizadas por la aplicación se encuentran en:

requirements.txt

💻 Ejecución local

Para ejecutar el proyecto en un entorno local, se recomienda utilizar un entorno virtual de Python.

1. Clonar el repositorio

Desde una terminal:

git clone <URL_DEL_REPOSITORIO>


Ingresar al directorio del proyecto:

cd <NOMBRE_DEL_REPOSITORIO>

2. Crear un entorno virtual

En Windows:

python -m venv venv
venv\Scripts\activate


En macOS/Linux:

python3 -m venv venv
source venv/bin/activate

3. Instalar las dependencias

Con el entorno virtual activado:

pip install -r requirements.txt


Esto instalará las librerías necesarias para ejecutar la aplicación.

4. Ejecutar la aplicación

Para iniciar Streamlit:

streamlit run app.py


Después de ejecutar el comando, Streamlit mostrará en la terminal una dirección local similar a:

Local URL: http://localhost:8501


Abre esa dirección en un navegador para acceder a la aplicación.

## Despliegue en Render

La aplicación fue desplegada utilizando Render.

Durante el despliegue, Render instala automáticamente las dependencias especificadas en:

requirements.txt


y ejecuta la aplicación mediante Streamlit.

La aplicación se encuentra disponible en:

https://tripletenmodule7.onrender.com

Configuración general

El proyecto requiere que el entorno de despliegue tenga acceso a:

app.py
vehicles_us.csv
requirements.txt


Estos archivos deben permanecer en el repositorio para que la aplicación pueda ejecutarse correctamente.

El puerto utilizado por Streamlit es el 8501, que corresponde al puerto detectado durante el despliegue.

# Visualizaciones

La aplicación incorpora diferentes recursos gráficos para facilitar la interpretación de los datos.

Histograma

El histograma permite observar la distribución de una variable determinada y facilita la identificación de concentraciones, dispersión y posibles valores extremos.

Gráfico de dispersión

El gráfico de dispersión permite analizar visualmente la relación entre dos variables y detectar posibles patrones o tendencias presentes en los datos.

Componentes interactivos

La aplicación también incorpora controles interactivos, como botones o casillas de verificación, para que el usuario pueda seleccionar o activar determinadas visualizaciones.

# Consideraciones sobre el despliegue

Durante el despliegue en Render puede aparecer un mensaje relacionado con:

Please replace `use_container_width` with `width`.


Este mensaje corresponde a una advertencia de compatibilidad/deprecación de Streamlit y no impide que la aplicación sea desplegada o utilizada.

La aplicación se encuentra disponible en:

https://tripletenmodule7.onrender.com

## Reproducibilidad

Para reproducir el proyecto localmente es necesario contar con:

El repositorio completo.

Python instalado.

El archivo vehicles_us.csv.

Las dependencias especificadas en requirements.txt.

El archivo app.py.

El flujo recomendado es:

vehicles_us.csv
       ↓
   EDA.ipynb
       ↓
Análisis y visualización
       ↓
     app.py
       ↓
 Aplicación Streamlit
       ↓
      Render
       ↓
Aplicación web pública

Autor: Antonio Jose Roodriguez Valencia

Proyecto de Ciencia de Datos — Proyecto 7

Este proyecto fue desarrollado como parte del programa de formación en Ciencia de Datos, aplicando técnicas de análisis exploratorio, visualización de datos y desarrollo de aplicaciones web interactivas.

## Licencia

Este proyecto fue desarrollado con fines educativos.


