#TALLER
#EJERCICIO1

# Ejercicio 1 - Registro de equipos

equipos=[] # lista

with open("equipos.txt","w") as archivo:
    for i in range(4):
        nom_Producto=input("Nombre del equipo: ")
        cantidad=int(input("Cantidad por unidad: "))
        valor_un=float(input("Valor de la unidad: "))
        equipo={ # diccionario
            "nombre":nom_Producto,
            "cantidad":cantidad,
            "valor":valor_un
        }
        equipos.append(equipo)        
        archivo.write(str(equipo["nombre"])+"," + str(equipo["cantidad"])+","+ str(equipo["valor"]) + "\n")




total_general = 0

with open("equipos.txt","r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        nom_Producto = datos[0]
        cantidad = int(datos[1])
        valor_un = float(datos[2])
        
        total = valor_un * cantidad
        total_general = total_general + total

        print(f"El producto {nom_Producto} tiene un valor total de ${total}")

        if total > 2000000:
            print(f"-> El equipo {nom_Producto} supera los $2.000.000")

print(f"\nValor total de todos los equipos: ${total_general}")