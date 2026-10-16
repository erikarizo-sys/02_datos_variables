#METODOS QUE MODIFICAN EL ESTADO DEL OBJETO
# class producto:
#     def __init__(self,nombre,cantidad):
#         self.nombre=nombre
#         self.cantidad=cantidad
#     def agregar_stock(self, unidades):
#         self.cantidad += unidades
# celular=producto("celular",2)

# celular.agregar_stock(5)

# print(celular.cantidad)



#CADA OBJETO CONSERVA SU PROPIO ESTADO

# class producto:
#     def __init__(self,nombre,cantidad):
#         self.nombre=nombre
#         self.cantidad=cantidad
#     def agregar_stock(self, unidades):
#         self.cantidad += unidades
# teclado=producto("teclado",3)        
# celular=producto("celular",2)
# mouse=producto("mouse",5)
# monitor=producto("monitor",2)
# mouse.agregar_stock(4) //se puede cambiar el estado de un objeto sin afectar a los demás objetos de la misma clase
# print(celular.cantidad)
# print(mouse.cantidad)
# print(monitor.cantidad)
# print(teclado.cantidad)



#ATRIBUTOS VS PARAMETROS
#No todo dato usado por un método debe guardarse como atributo
# class producto:
#     def __init__(self,nombre,precio):
#         self.nombre=nombre
#         self.precio=precio
#     def calcular_total(self, cantidad):
#         return  self.precio * cantidad
    
# teclado=producto("teclado",20000)        
# celular=producto("celular",35000)
# mouse=producto("mouse",5000)
# monitor=producto("monitor",23000)
# # mouse.agregar_stock(4)
# mouse.calcular_total(5)
# # print(celular.cantidad)
# print(mouse.calcular_total(4))
# print(monitor.cantidad)
# print(teclado.cantidad)
#los parametros toma valores como argumentos, mientras que los atributos son variables que pertenecen a un objeto y se pueden acceder desde cualquier método de la clase.




##DICCIONARIO VS OBJETO
#Ambos organizan datos, pero los objetos también pueden tener comportamiento (métodos) y encapsular datos y funciones relacionadas, mientras que los diccionarios solo almacenan datos sin comportamiento asociado.


##CREAR UNA CLASE PRODUCTO COMPLETA
#La clase PRODUCTO define qué datos guardará cada producto y que acciones se podrán realizar con ellos, es decir, define el comportamiento de los objetos de la clase PRODUCTO
# class Producto:
#     def __init__(self,nombre,precio,cantidad): #parámetros
#         self.nombre=nombre #parámetros, self.nombre es un atributo del objeto
#         self.precio=precio #parámetros, self.precio es un atributo del objeto
#         self.cantidad=cantidad #parámetros, self.cantidad es un atributo del objeto
#     def agregar_stock(self, unidades): #def, método que modifica el estado del objeto
#         self.cantidad += unidades
#     def calcular_total(self, cantidad):
#         return  self.precio * cantidad
#     def mostrar_datos(self):
#         return f"{self.nombre}-{self.precio}-{self.cantidad}"
#     def calcular_total(self):
#         return self.precio * self.cantidad
# mouse=Producto("Mouse",5000,5)
# teclado=Producto("Teclado",20000,3)
# monitor=Producto("Monitor",23000,2)
# print (mouse.mostrar_datos())
# print (teclado.calcular_total())
# mouse.agregar_stock(2)
#objeto= clase("")


##ERRORES COMUNES EN POO
#Detectar estos errores ayuda a depurar más rápido
#1.Está self?
#2.¿Se está usando el nombre del objeto?
#3.¿Se está usando el nombre de la clase?
#4.¿El atributo tiene self.?
#5.¿El return es necesario?

#EJERICIO: RETO FINAL
class cuenta_bancaria:
    def __init__(self,titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def consultar_saldo(self):
        return self.saldo    
    def depositar(self,monto):
        self.saldo += monto
    def retirar(self,monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Saldo insuficiente")
    def mostrar_datos(self):
        return f"Titular:{self.titular}, Saldo:{self.saldo}"
cuenta1 = cuenta_bancaria("Carlos", 1000000) #objetos
cuenta2= cuenta_bancaria("Ana", 50000)

cuenta1.depositar(50000)
cuenta1.retirar(30000)
cuenta2.retirar(60000)
print(cuenta1.mostrar_datos())
print(cuenta2.mostrar_datos())

    







