import streamlit as st

#python -m pip install streamlit
st.title("Análisis de Distancias") #titulo del dashboard
st.write("Bienvenido al primer dashboard de análisis de distancias") #descripcion del dashboard

distancia=st.slider("Seleccione la distancia en cm", 0, 50, 20) #slider para seleccionar la distancia
st.write("La distancia seleccionada es:", distancia) #muestra la distancia seleccionada

#python -m streamlit run 28_dashboard.py
#F5 para que se actualice automáticamente

if distancia < 20:
   st.write("Objeto cerca")
else:
  st.write("Distancia Segura")
import pandas as pd
datos={
    "Medición": [1, 2, 3, 4, 5, 6, 7, 8],
    "Distancia": [15, 18, 22, 12, 30, 25, 28, 10, 20]
}
tabla=pd.DataFrame(datos) #crea un dataframe a partir del diccionario datos
st.subheader("Registro de mediciones") #subtitulo del dashboard
st.dataframe(tabla) #muestra el dataframe en el dashboard

st.subheader("Gráfica de distancias") #subtitulo del dashboard

st.line_chart(tabla, x="Medición", y="Distancia") #grafica de lineas de la columna Distancia del dataframe
tabla["Distancia Ajustada"]=tabla["Distancia"]+2 #crea una nueva columna en el dataframe, con los valores de la columna Distancia multiplicados por 2

opcion=st.selectbox("Seleccione una opción", ["Distancia Original", "Distancia Ajustada"]) #selectbox para seleccionar la columna a graficar
st.line_chart(tabla, x="Medición", y=opcion) #grafica de lineas de la columna seleccionada

cantidad=st.select_slider("Cantidad de mediciones: ", 1, 8, 9 ) #selectslider para seleccionar la cantidad de mediciones a mostrar
tabla filtrada= tabla.head(cantidad) #filtra el dataframe para mostrar solo las primeras n filas