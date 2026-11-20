import pandas as pd #libreria para trabajar con textos
 #python  -m pip install pandas
datos={
    "Medición": [1, 2, 3, 4, 5],
    "Distancia": [15, 18, 22, 12, 30]
 }
tabla_datos=pd.DataFrame(datos) #crea un dataframe a partir del diccionario datos
print(tabla_datos) #imprime el dataframe

print(tabla_datos["Distancia"]) #imprime la columna Distancia del dataframe
promedio=tabla_datos["Distancia"].mean()
print(promedio)
dis_max=tabla_datos["Distancia"].max()# a diferencia de numpy, pandas tiene metodos para trabajar con los datos del dataframe
print(dis_max)
temp_altas=tabla_datos[tabla_datos["Distancia"]>20] #filtra los datos del dataframe, y devuelve un nuevo dataframe con los datos que cumplen la condicion
print(temp_altas)
tabla_datos["Distancia Doble"]=tabla_datos["Distancia"]*2 #crea una nueva columna en el dataframe, con los valores de la columna Distancia multiplicados por 2
print(tabla_datos)
tabla_datos.to_csv("datos.csv", index=False) #guarda el dataframe en un archivo csv, sin el indice