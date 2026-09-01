#Ejercicio 1
nombrecliente = input( "Nombre del Cliente")
producto= input("Producto")
precioun= float(input("Precio unitario ")) 
cantidad=int(input("Cantidad"))

total= precioun*cantidad

print("Nombre: ", nombrecliente)
print("Producto: ",producto)
print("Cantidad: ",cantidad)
print("Precio unidad: ",precioun)
print("Total compra: ",total)




#Ejericio 2


nombre = input("Nombre: ")
edad = int(input("Edad: "))
temperatura = float(input("temperatura corporal: "))
nota = float(input("nota obtenida es de 0.0 a 5.0: "))
carnet = input(" tiene carnet? si o no: ")


mayor_edad = edad >= 18
temp_adecuada = 36.0 <= temperatura <= 37.5
cap_aprobada = nota >= 3.0
tiene_carnet = carnet == "si"

cumple_requisitos = mayor_edad and temp_adecuada and cap_aprobada and tiene_carnet

print("mayor_edad", mayor_edad)
print("temp_adecuada",temp_adecuada)
print("cap_aprobada",cap_aprobada)
print("tiene_carnet",tiene_carnet)


#ejercicio con if anidado
edad=25
matricula="si"
contraseña="azul"
if edad < 18:
    print("Acceso restringido")
else:  # pertenece alk if de arriba
    if matricula == "si":
        if contraseña == "azul21":
            print("Bienvenido")
        else    
            print("Contrase;a incorrecta")
    else:
        print ("No matriculado")       
