# #Ejercios con if y else
edad=20
if edad>=18:
    print("puede ingresar")    
else:
    print("Menor de edad")

nota=4.3
if nota >=3.0:
    print("Insuficiente")    
elif nota <4.0:
    print("Básico") 
elif nota <4.6:
    print("Alto")   
else:
    print("Superior")

nota=4.8
if nota>=3.0:
    print("Aprobado")
elif nota <4.5:
    print("Excelente")    


nota=float(input("Nota")) 
if nota <0 or nota >5:    
    print("Nota no valida")
elif nota <3:
    print("Insuficiente")
elif nota <4:
    print("Básico")
elif nota <4.6:
    print("Alto")
else:
    print("Superior")


# ejercicio con if anidado
edad=25
matricula="si"
contraseña="azul21"
if edad < 18:
    print("Acceso restringido")
else:  # pertenece alk if de arriba
    if matricula == "si":
        if contraseña == "azul21":
            print("Bienvenido")
        else:  
            print("Contraseña incorrecta")
    else:
        print ("No matriculado")     

# #Ejericio 2

nombre=input("Ingrese el nombre:")
edad=int(input("Ingrese su edad"))
invitación=input("Tiene invitació? si o no")
invitación= invitación.lower() #Convierte la mayúscula en minuscula
if edad >= 18 and invitación == "si": 
    print("Autorizado",nombre)
else:  # pertenece alk if de arriba
    if edad >18 and invitación == "no":
        print("invitación", invitación)
        print("Necesita invitación")
        if edad == "< 18":
            print("Acceso denegado")

#Ejercicio 3 (while)
numero=1
while numero <=5:
    print("Numero",numero)
    numero=numero+1

# #Ejericio 4( contador)    
contador=1
while numero <=5:
    print("Contador",contador)
    numero=numero+1

# #Ejericio 5
numero=1
while numero <=3:
    print(numero) 
#para detener el ciclo, ctrl,c en la terminal       

#Ejericio 6
contraseña =""
while contraseña!="python":
    contraseña=input("contraseña:")
print("Bienvenido")    

# #Ejericio 7
contraseña =""
intentos = 0
while contraseña!="python" and intentos <3:
     contraseña=input("contraseña:")
     intentos=intentos+1
if contraseña == "python":
    print("Acceso autorizado")
else:
    print("Acceso bloqueado")   

#Ejericio 8

pin = ""
intentos = 0
while pin != "2580" and intentos <3:
     pin =  input("El pin es ")

     intentos=intentos+1
if pin == "2580":
    print("Acceso a la cuenta")
else:
    print("Tarjeta bloqueada")     