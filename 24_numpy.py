import numpy as np #libreria para trabajar con arrays
# python -m pip install numpy
# temperaturas=np.array([26, 28, 31, 29, 25, 33, 27])

# temp_aumentadas=temperaturas + 2
# promedio=np.mean(temperaturas)# , mean para aumentar el promedio de los valores del array
# tem_max=np.max(temperaturas)
# temp_min=np.min(temperaturas)

# print(temp_aumentadas)
# print(promedio)
# print(tem_max)
# print(temp_min)
# print(temperaturas[0])
# print(temperaturas[6])
# temp_bajas=temperaturas[temperaturas<28], #comparaciones como el if
# print(temp_bajas)
# tem_altas=temperaturas[temperaturas>29]
# print(tem_altas)

temperaturas=np.array([[20, 21, 19, 22, 20, 21, 19]]) #array de 2 dimensiones
suma=np.sum(temperaturas) #suma de todos los valores del array
promedio=np.mean(temperaturas) #promedio de todos los valores del array
media_estandar=np.std(temperaturas) #desviacion estandar de todos los valores del array
print(suma)
print(round(promedio,2)) #con un redondeo de 2 decimales
print(round(media_estandar,2))

##nupy, es una libreria para trabajar con arrays, que permite realizar operaciones matematicas y estadisticas de manera eficiente.