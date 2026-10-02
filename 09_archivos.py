#archivos permiten guardar información, agregar datos, modificarlos
#modo r para leer,w para write,a para append(agregar) 
#r lee w- empieza de cero- a agrega
#SE DEBE CREAR PRIMERO UNA CARPETA PARA QUE SE PUEDA LEER EL ARCHIVO

#Abrir un archivo -1 manera
# archivo = open("SALUDO.txt")
# contenido = archivo.read()
# print(contenido)#siempre que se abre un archivo se debe cerrar
# archivo.close()

# #Abrir un archivo -2 manera
# with open("SALUDO.txt","r") as archivo: #variable archivo
#     texto = archivo.read()
#     print(texto)
#     #de esta manera no es necesario cerrar el archivo


# with open("datos.txt","w") as archivo: #w escribir o crear archivo
#     archivo.write("Ana")
# with open("datos.txt","r") as archivo:
#     texto = archivo.read()
# print(texto)# fuera de la identación para que se cierre el archivo


# #a para agregar información al archivo
# with open("registro.txt","w") as archivo:
#     archivo.write("Ana\n")
# with open("registro.txt","a") as archivo:
#     archivo.write("Luis\n")
#     archivo.write("Carlos\n")# slash invertido y n, salto de linea
# with open("registro.txt","r") as archivo:
#     texto = archivo.read()
# print(texto)

#leer linea por linea
# with open("registro.txt","r") as archivo:
#     for linea in archivo:
#         print(linea.strip())#strip elimina los espacios de linea al imprimir el codigo
# print("Final")



# #Todo LO LEIDO DESDE .TXT LLEGA COMO TEXTO(STR), se hace la conversion del dato
# with open("edad.txt","w") as archivo:
#     archivo.write("20\n")
#     archivo.write("25\n")
#     archivo.write("30\n")
# with open("edad.txt","r") as archivo:
#     for linea in archivo:
#         edad = int(linea.strip())#convertir a entero
#         print(edad+5)
# #se lee, se recorre en archivos, se crea variable edad, se convierte a entero y se le suma 5, se imprime el resultado
# print("Final")# para finalizar el archivo y que no se quede abierto, se imprime fuera de la identación


#TRES FORMAS DE LEER UN ARCHIVO
# 1. read() - Lee todo el contenido del archivo
# 2. readline() - Lee una línea del archivo
# 3. readlines() - Lee todas las líneas del archivo y las devuelve como una lista
# with open("registro.txt","r") as archivo:
#     datos = archivo.readlines()
#     print(datos[1].strip())#imprime la segunda linea del archivo


#ESCRIBIR LISTAS EN ARCHIVOS, si ya se tiene una lista se recorre y escribe cada elemento
# productos = ["Mouse","Teclado","Monitor",]
# with open("productos.txt","w") as archivo:
#     for producto in productos:
#         archivo.write(producto + "\n")
# #La list queda guardada en el programa, mientras que el archivo queda guardado en la carpeta del proyecto, se puede abrir y ver el contenido

# #WRITELINES():utiliza para escribir una lista en un archivo, se puede usar para escribir una lista de strings en un archivo de texto.
# with open("nombres.txt","w") as archivo:
#     archivo.writelines(["Ana\n","Luis\n","Carlos\n"])#writelines recibe una lista de strings y los escribe en el archivo, se puede usar para escribir una lista de strings en un archivo de texto.
#     #writelines no agrega salto de linea, se debe agregar manualmente con \n


# #GUARDAR REGISTROS SEPARADOS POR COMA, una liena puede tener varios campos:nombre, precio, cantidad
# productos = [
#     {"nombre":"Mouse","precio":50000,"cantidad":5},
#     {"nombre":"Teclado","precio":80000,"cantidad":3}   
# ]
# with open("productos.txt","w") as archivo:
#     for producto in productos:
#         archivo.write(producto["nombre"]+","+
#                       str(producto["precio"])+","+
#                       str(producto["cantidad"])+"\n")#se guarda en el archivo productos.txt, cada producto en una linea, separado por coma+




# #LEER UN REGISTRO CON SPLIT(",")- divide un texto según un separador, en este caso la coma, y devuelve una lista con los elementos separados
with open("productos.txt","r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")#separa la linea en una lista de strings, separados por coma
        nombre = datos[0]#se guarda el primer elemento de la lista en la variable nombre
        precio = int(datos[1])#se guarda el segundo elemento de la lista en la variable precio
        cantidad = int(datos[2])#se guarda el tercer elemento de la lista en la variable cantidad
        total = precio * cantidad
        print("Producto:",nombre,"Precio:",precio,"Cantidad:",cantidad,"Total:",total)


