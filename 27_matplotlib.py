import pandas as pd
import matplotlib.pyplot as plt
#python  -m pip install matplotlib

tabla=pd.read_csv("datos.csv") #lee el archivo csv y lo guarda en un dataframe
plt.plot(tabla["Medición"], tabla["Distancia"])# grafica de manera lineal
plt.bar(tabla["Medición"], tabla["Distancia"]) # grafica de barras
plt.xlabel("Medición")# la etiqueta del eje x
plt.ylabel("Distancia") #la etiqueta del eje y
plt.title("Distancia medidas por el HC-SR04")# titulo del grafico
plt.show() #muestra el grafico
