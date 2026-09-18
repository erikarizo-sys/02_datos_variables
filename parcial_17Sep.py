# #PRIMER PUNTO-PARTE A
# edad= int(input("Ingerse su edad:"))
# if edad>=18:
#     print("Mayor de edad")
# else:
#     print("Menor de edad")

#En esta parte se le agrega un int ya que se esta ingresando un valor entero

#PRIMER PUNTO- PARTE B
# nota=float (input("Ingrese la nota:"))
# if nota>=4.5 and nota>=5:
#     print("Desempeño superior")
# if nota>=3 and nota<4.5:
#     print ("Aprobado")
# if nota<3:
#     print("No aprobado")    


#SEGUNDO PUNTO
   
# nota=float(input("Ingrese la nota:"))
# if nota<0.0 or nota>5.0:
#     print("Nota invalida")
# elif nota<3.0:
#     print("No aprobado")
# elif nota<=4.0:
#     print("Desempeño básico")
# elif nota<=4.6:
#     print("Desempeño alto")
# else:
#     print("Desempeño superior")

total_ventas=0
cantidad_ventas=0
opcion=0
while opcion!=3:
    print("1. Registrar venta")
    print("2. Consultar resumen")
    print("3. Salir")
    opcion=int(input("Ingrese la opción:"))
    if opcion==1:
        venta=float(input("Ingrese el valor de la venta:"))
        total_ventas+=venta
        cantidad_ventas+=1
        print("Venta registrada")
    elif opcion==2:
        print("Cantidad de ventas", cantidad_ventas)
        print("Total vendido", total_ventas)
    elif opcion==3:
        print("Registro finalizado")
        print("Cantidad de ventas",cantidad_ventas)
        print("Total vendido", total_ventas)
    else:
        print("Opción inválida")