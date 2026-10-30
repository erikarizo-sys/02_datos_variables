#PARTE B- MANEJO DE ARCHIVOS 

# print("INGRESE LA SIGUIENTE INFORMACIÓN: ")
# productos=[]


# with open("productos.txt","w") as archivo:
#     for i in range(3):
#         nom_Producto=input("Nombre del equipo: ")
#         cantidad=int(input("Cantidad por unidad: "))
#         valor_un=float(input("Valor de la unidad: "))
#         producto={ 
#             "nombre":nom_Producto,
#             "cantidad":cantidad,
#             "valor":valor_un
#         }
#         productos.append(producto)        
#         archivo.write(str(producto["nombre"])+"," + str(producto["cantidad"])+","+ str(producto["valor"]) + "\n")

# total_general = 0

# with open("productos.txt","r") as archivo:
#     for linea in archivo:
#         datos = linea.strip().split(",")
#         nom_Producto = datos[0]
#         cantidad = int(datos[1])
#         valor_un = float(datos[2])
        
#         total = valor_un * cantidad
#         total_general = total_general + total

#         print(f"El producto {nom_Producto} tiene un valor total de ${total}")

#         if total > 200000:
#             print(f" El producto {nom_Producto} supera los $200.000")

# print(f"\nValor total de todos los equipos: ${total_general}")


#PARTE C-POO

class Dispositivo:
    def __init__(self, nombre, marca, precio):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio

    def mostrar_info(self):
        print(f"{self.nombre}  {self.marca}  ${self.precio}")

    def calcular_descuento(self, porcentaje): 
        return self.precio - (self.precio * porcentaje)

class Sensor(Dispositivo):
    def __init__(self, tipo, unidad, estado):
        super().__init__(nombre, marca, precio)
        self._tipo = tipo
        self._unidad =unidad
        self.__estado = "Activo" 
        self.cambiar_estado(estado)

    def cambiar_estado(self, nuevo):
        if nuevo in ["Activo", "Inactivo"]:
            self.__estado = nuevo
        else:
            print(f"Error: '{nuevo}' no es válido. Solo Activo o Inactivo.")

    def consultar_estado(self):
        return self.__estado

    def mostrar_info(self):
        print(f"Sensor: {self.nombre}  Marca del sensor: {self.marca}  Precio del sensor: ${self.precio}  Tipo: {self._tipo} Unidad:{self._unidad} Estado: {self.__estado}")


dispo1 = Sensor("Sensor Ultrasonico", "Orejitas", 17000, 3, "Activo")
dispo2= Sensor("Sensor de Movimiento", "Salsa", 20000, 5, "Activo")


print("\nCambiando Dispositivo1 a Prestado:")
dispo1.cambiar_estado("No hay")
print("Estado actual:", dispo1.consultar_estado())

print("\nIntentando poner estado 'Dañado':")
dispo1.cambiar_estado("Inactivo")
print("Estado actual:", dispo1.consultar_estado())

print(f"\nPrecio con 10% descuento en PC1: ${dispo1.calcular_descuento(0.10)}")
    