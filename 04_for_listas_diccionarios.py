# total = 0
# for vueltas in range(4):
#      numero = int(input("numero: "))
#      total = total + numero
# print ("Numero:", numero)     

# contador = 0
# suma = 0 
# for numero in range (1,11):
#     if numero % 2 == 0:
#         contador += 1
#         suma += numero
# print("cantidad de pares :", contador)    
# print("suma de pares :" , suma )  




# for numero in range (1,8 ):
#     if numero ==4:
#         print(numero)


# texto = "Hola"

# for letra in texto:
#     print("letra: ", letra)

# texto = "Area Tecnica"
# texto = texto.lower()
# for letra in "aeiouáéíóú":
#     cantidad = texto.count(letra)

# texto = "Python" ## en paiton numera desde el cero, sirve para los indicies, para ubicar mas facilmente las letras de una palabra, y tambien sirve para hacer rebanadas de palabras, es decir, cortar palabras en partes.

# len(texto) #6
# texto[0] #P
# texto[-1] #n
# texto[0:3] #Pyt
# texto[::-1] #thon


# ##listas 

# notas = [4.5, 3.8, 5.0, 2.9] #las listas usan corchetes 
# print(notas[0]) #4.5
# print(notas[-1]) #5.0 en tonces menos uno es de derecha aizquierda 
# print(len (notas)) #5 aqui cuenta la cantidsad de elementos que hay en la lista, en este caso 5


# notas = [4.5, 3.0, 5.0]
# for nota in notas:
#     print("nota:", nota) 

# suma = 0
# for nota in notas:
#     suma += nota
# promedio = suma / len(notas)
# print("Promedio:", promedio)

# notas = []
# for vueltas in range(3):
#     nota = float(input("Ingrese la nota: "))
#     notas.append(nota) #append sirve para agregar elementos a la lista  

# print(notas) #se imprime en corchetes


# frutas=["manzana", "pera", "uva"]
# frutas [1] = "mango"
# #["manzana", "pera", "uva"]
# print("frutas:", frutas)
# frutas.remove("uva") #elimina un valor

#HERRAMIENTAS ÚTILES EN LISTAS
# numeros = [30, 10, 40, 20]
# print(numeros)
# numeros.sort() #modifica la lista
# print(numeros)
# ordenada=sorted(numeros)# crea otra lista
# print(numeros)
# numeros.reverse () #invierte el orden actual
# print(numeros)
# numeros.count (20) #cuenta coincidencias
# print(numeros.count(20))
# numeros.index (40) #primera posición donde aparece
# print(numeros.index(40))


# #Cuando necesito la posición
# nombres= ["Ana", "Luis", "Carlos" ] #posición inicial i, se va sumando de a uno y se va enumerando
# for i in range(len(nombres)): #len cuenta los datos de la lista
#     print("Estudiante", i+1, ":", nombres [i])


# notas=[2.5, 3.0, 4.0, 1.8]  #al hacer el recorrido tiene en cuenta los signos (<,>) para imprimir la nota correspondiente
# for i in range (len(notas)):
#     if notas[i] <3.0:
#         notas[i] = 3.0
# print (notas)     


# #Listas anidadas
# estudintes= [
#     ["Ana", 4.5],
#     ["Luis", 3.8],
#     ["Carlos", 4.2]
# ]
# print("Estudiantes", estudintes)
# for estudiante in estudintes:
#     print(estudiante[0], estudiante[1])

estudiantes =[
    ["Ana", [4.0, 3.5, 5.0]],
    ["Luis", [2.8, 3.0, 4.2]],
]
for estudiante in estudiantes:
    suma = 0
    for nota in estudiante [1]:
        suma += nota
    promedio = suma / len(estudiante[1])    
    print(estudiante[0],round(promedio, 2))