import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

#Modifica los nombres de los campos a minusculas
# Bucle que itera sobre los encabezados y los pone todos en minúsculas
new_col_names = []

for column in car_data.columns:
    #las letras en minúsculas
    name_lowered = column.lower()
    new_col_names.append(name_lowered)

# Reemplaza los nombres anteriores por los nuevos
car_data.columns = new_col_names


#Ajusto los valores ausentes del paint_color a 'Unknown' ya que no se puede determinar el color de pintura del vehiculo 
ausentes = car_data[car_data['paint_color'].isna()]

if (len(ausentes) > 0):
    #print(ausentes)
    car_data['paint_color'] = car_data['paint_color'].fillna('Unknown')


#Ajusto los valores ausentes del is_4wd a 0.0 (False) ya que la mayoria de los vehiculos no son 4WD
ausentes = car_data[car_data['is_4wd'].isna()]

if (len(ausentes) > 0):
    #print(ausentes)
    car_data['is_4wd'] = car_data['is_4wd'].fillna(0.0)


#Ajusto los valores ausentes del model_year, se reemplaza por la mediana de todos los años
ausentes = car_data[car_data['model_year'].isna()]
if (len(ausentes) > 0):
    #print(ausentes)
    car_data['model_year'] = car_data['model_year'].fillna(car_data['model_year'].median())

#Ajusto los valores ausentes del odometer segun el model_year, se reemplaza por la mediana de cada año
ausentes = car_data[car_data['odometer'].isna()]
if (len(ausentes) > 0):
    car_data['odometer'] = car_data.groupby('model_year')['odometer'].transform(lambda x: x.fillna(x.median()))

#En caso de que no se pueda calcular la mediana por año, se reemplaza por la mediana general
ausentes = car_data[car_data['odometer'].isna()]
if (len(ausentes) > 0):
    car_data['odometer'] = car_data['odometer'].fillna(car_data['odometer'].median())


#Ajusto los valores ausentes del cylinders, se reemplaza por la mediana de todos los cilindros
ausentes = car_data[car_data['cylinders'].isna()]
if (len(ausentes) > 0):
    car_data['cylinders'] = car_data['cylinders'].fillna(car_data['cylinders'].median())

#transformo la columna date_posted a tipo fecha
car_data['date_posted'] = pd.to_datetime(car_data['date_posted'])



# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')
hist_button1 = st.button('Construir grafico de dispersión')


# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button1:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un scatter plot utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de scatter
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Relación entre Odómetro y Precio')

    # Mostrar el gráfico Plotly
    st.plotly_chart(fig, use_container_width=True)


