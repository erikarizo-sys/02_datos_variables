#TALLER
#EJERCICIO1

# equipos=[] # lista

# with open("equipos.txt","w") as archivo:
#     for i in range(4):
#         nom_Producto=input("Nombre del equipo: ")
#         cantidad=int(input("Cantidad por unidad: "))
#         valor_un=float(input("Valor de la unidad: "))
#         equipo={ # diccionario
#             "nombre":nom_Producto,
#             "cantidad":cantidad,
#             "valor":valor_un
#         }
#         equipos.append(equipo)        
#         archivo.write(str(equipo["nombre"])+"," + str(equipo["cantidad"])+","+ str(equipo["valor"]) + "\n")




# total_general = 0

# with open("equipos.txt","r") as archivo:
#     for linea in archivo:
#         datos = linea.strip().split(",")
#         nom_Producto = datos[0]
#         cantidad = int(datos[1])
#         valor_un = float(datos[2])
        
#         total = valor_un * cantidad
#         total_general = total_general + total

#         print(f"El producto {nom_Producto} tiene un valor total de ${total}")

#         if total > 2000000:
#             print(f"-> El equipo {nom_Producto} supera los $2.000.000")

# print(f"\nValor total de todos los equipos: ${total_general}")

#EJERICIO 2


class Dispositivo:# CLase Dispositivo
    def __init__(self, nombre, marca, precio):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio

    def mostrar_info(self):
        print(f"{self.nombre}  {self.marca}  ${self.precio}")

    def calcular_descuento(self, porcentaje): # 0.10 = 10%
        return self.precio - (self.precio * porcentaje)

class Computador(Dispositivo):
    def __init__(self, nombre, marca, precio, memoria_ram, estado):
        super().__init__(nombre, marca, precio)
        self.memoria_ram = memoria_ram
        self.__estado = "Disponible" 
        self.cambiar_estado(estado)

    def cambiar_estado(self, nuevo):
        if nuevo in ["Disponible", "Prestado"]:
            self.__estado = nuevo
        else:
            print(f"Error: '{nuevo}' no es válido. Solo Disponible o Prestado.")

    def consultar_estado(self):
        return self.__estado

    def mostrar_info(self):
        print(f"Computador: {self.nombre}  Marca: {self.marca}  Precio: ${self.precio}  RAM: {self.memoria_ram}GB  Estado: {self.__estado}")

    def tiene_16_o_mas(self):
        return self.memoria_ram >= 16

pc1 = Computador("Gamer Asus", "Asus", 3500000, 16, "Disponible")# Objetos
pc2 = Computador("Oficina Lenovo", "Lenovo", 2000000, 8, "Disponible")

pc1.mostrar_info()
print("¿16GB o más?", pc1.tiene_16_o_mas())
pc2.mostrar_info()
print("¿16GB o más?", pc2.tiene_16_o_mas())

print("\nCambiando PC1 a Prestado:")
pc1.cambiar_estado("Prestado")
print("Estado actual:", pc1.consultar_estado())

print("\nIntentando poner estado 'Dañado':")
pc1.cambiar_estado("Dañado")
print("Estado actual:", pc1.consultar_estado())

print(f"\nPrecio con 10% descuento en PC1: ${pc1.calcular_descuento(0.10)}")

