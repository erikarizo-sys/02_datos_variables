#CONTINUACIÓN ARCHIVOS 2 PARTE

#productos = [
#     {"nombre":"Mouse","precio":50000,"cantidad":5},
#     {"nombre":"Teclado","precio":80000,"cantidad":3}, 
#     {"nombre":"Monitor","precio":700000,"cantidad":2},     
# ]
# with open("productos.txt","w") as archivo:
#     for producto in productos:
#         archivo.write(producto["nombre"]+","+
#                       str(producto["precio"])+","+
#                       str(producto["cantidad"])+"\n")


#EJERCICIO
# with open("estudiantess.txt","w") as archivo:
#     for i in range (3):
#         nombre=input("Ingrese el nombre:")
#         edad=int(input("Ingrese la edad:"))
#         archivo.write(nombre + "," + str(edad) +  "\n")
# estudiantes = []
# with open("estudiantess.txt","r") as archivo:
#     for linea in archivo:
#         datos = linea.strip().split(",")#separa el nombre y la edad por la coma
#         estudiante={"nombre":datos[0],
#                     "edad":int(datos[1])
#                     }
#         estudiantes.append(estudiante)
#         print(estudiante)



# PROGRAMACIÓN ORIENTACIÓN A OBJETOS-POO

# class Producto:
#     pass #definición de la clase Producto, sirve para ejecutar el código
# mouse=Producto() #producto es la clase
# teclado=Producto()# teclado es un objeto de la clase Producto
# print(type(mouse))

# #EL CONSTRUCTOR __init__() - se ejecuta automáticamente al crear un objeto de la clase, sirve para inicializar los atributos del objeto
# class Producto:
#     def __init__(self,nombre,precio): #def, definir una función
#         self.nombre=nombre #self representa al objeto que está usando el método en ese momento, se usa para acceder a los atributos y métodos del objeto
#         self.precio=precio #self no se asigna, lo hace automáticamente Phyton
# mouse=Producto("Mouse",50000)        
# #atributos, donde se va a guardar la información del objeto


#ATRIBUTOS DEL OBJETO-un atributo es información que pertenece a un objeto
# class Producto:
#     pass
#     def __init__(self,nombre,precio,cantidad):
#         self.nombre=nombre #nombre, se guarda en self.nombre, que es un atributo del objeto, se puede acceder a él desde cualquier método de la clase
#         self.precio=precio
#         self.cantidad=cantidad
# teclado=Producto("Teclado",80000,3)
# print("Producto:teclado.nombre, Precio:teclado.precio, Cantidad: teclado.cantidad")
        

#METODOS:FUNCIONES DENTRO DE UNA CLASE
#Un metodo representa una acción que puede realizar el objeto
class Producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
        
    def demostrar_precio(self):
        print(self.nombre,self.precio)
mouse=Producto("Mouse",50000)
mouse.demostrar_precio()#se llama al metodo demostrar_precio, que imprime el nombre