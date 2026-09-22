# def presentar(nombre, edad):
#     print ("Nombre", nombre)
#     print ("Edad", edad)
# presentar ("Laura",22)  // print muestra- return devuelve

# def sumar(a,b):
#     print(a+b)

# resultado=sumar(5,3)
# print(resultado)

# def multiplicar(a,b):
#     return a*b 
# resultado=multiplicar(4,5)+10 #poner los valores para evitar la función
# print(resultado)

# def calcular_promedio(notas):
#     suma=0
#     for nota in notas:
#         suma+=nota
#     return suma/len(notas) #len, cuenta tanto caracteres como otros elementos de una lista
# notas_ana=[4.0,3.5, 5.0]
# promedio=calcular_promedio(notas_ana)
# print(round(promedio,2)) #round redondea el valor a 2 decimales

# def calcular():
#     resultado=20
#     print(resultado)
# calcular()
# print(resultado) #no se puede imprimir la variable resultado ya que esta dentro de la función y no es global

# nombre="Laura"
# def saludar():
#     global nombre #para que la variable nombre sea global y pueda ser usada fuera de la función
#     print("Hola", nombre)
# saludar()

# contador=10
# def aumentar():
#     global contador
#     contador=contador+1
#     print(contador)
#     aumentar()

# def aumentar(numero):
#     return numero+1
# contador=10
# contador=aumentar(contador)
# print(contador)

#EJERICIO-
# def calcular_total(precio, cantidad): #precio y cantidad son parametros(patametro en la función)
#     return precio*cantidad
# producto={
#     "nombre":"teclado", #{}-diccionario, en diccionario no están los indices, sino por claves
#     "precio":80000,
#     "cantidad":3
# }
# producto["total"]=calcular_total(
#     producto["precio"],
#     producto["cantidad"]
# )
# print(producto)


# def sumar_puntos(puntos):
#     return puntos+10
# puntos=5
# puntos=sumar_puntos (puntos)
# print(puntos)

#TALLER
# estudiantes=[
#     {"nombre":"Ana", "nota":[4.0,3.5,5.0]},  
#     {"nombre":"Luis", "nota":[2.5,3.0,2.8]}
#     {"nombre":"Carlos", "nota":[4.5,4.0,4.8]}
# ]
   





#TALLER

estudiantes=[
    {"nombre":"Ana", "nota":[4.0,3.5,5.0]},  
    {"nombre":"Luis", "nota":[2.5,3.0,2.8]},
    {"nombre":"Carlos", "nota":[4.5,4.0,4.8]}
]
def calcular_promedio(notas):
    suma=0
    promedio=sum(notas)/len(notas)
    return promedio
    promdioestudiantes =calcular_promedio(estudiante[1]["nota"])
    print(round(promedioestudiantes,2))
for estudiante in estudiantes:
    promedio = calcular_promedio(estudiante["nota"]) 
   
  
    if promedio>=3.0:
        estado="Aprobado"
    else:
        estado="No aprobado"
    estudiante["promedio"]=round(promedio,2)
    estudiante["estado"]=estado    
print(estudiantes)
       





