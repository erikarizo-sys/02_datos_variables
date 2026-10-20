#DE LA CLASE PADRE A CLASE HIJA
#La herencia permite reutilizar código cuando varias clases comparten carácterísticas similares. La clase hija hereda los atributos y métodos de la clase padre, lo que facilita la creación de nuevas clases sin tener que reescribir el código existente.
# class Persona:
#     def __init__(self, nombre,):
#         self.nombre = nombre 

#     def saludar(self):
#         return (f"Hola,soy {self.nombre} ")
# class Estudiante(Persona): #el padre(Persona) es la clase de la que se hereda, y Estudiante es la clase hija que hereda los atributos y métodos de Persona.
#         pass
# estudiante1 = Estudiante("Erika")
# print(estudiante1.saludar())#independientemente de que la clase Estudiante no tenga el método saludar, puede acceder al método saludar de la clase Persona, ya que hereda de ella.
#Una clase con pass puede usar atributos y métodos heredados


#PARA QUE SIRVE SUPER()
#super() permite ejecutar el constructor o los métodos de la clase padre
# class Persona:
#      def__init__(self, nombre, edad)
#      self.nombre=nombre
#      self.edad=edad
# class Estudiante(Persona):
#      def__init__(self, nombre, edad, carrera):
#      super().__init__(nombre, edad)
#      self.carrera=carrera
# estudiante1=Estudiante("Erika,24,Lic.Tecnología")


#ATRIBUTOS HEREDADOS Y PROPIOS
#La clase hija puede conservar lo heredado y agreagr información nueva
# class Estudiante(Persona):
#      def__init__(self,nombre,edad,carrera,nota):
#      super().__init__(nombre,edad)
#      self.carrera=carrera
#      self.__nota=nota
# estudiante1=Estudiante("Luis", 34, "Lic.Tecnología, 4.5")
# # estudiante1.presentarse()
# # #metodo heredado de persona 
# # estudiante1.mostrar_nota()
# # #metodo propio del estudiante
# # estudiante1.obtener_estado()
# # #metodo propio del estudiante

#SOBREESCRITURA DE MÉTODOS
#La clase hija puede redefinir un método heredado para tener un comportamiento propio
# class Persona:
#     def presentarse(self):
#         return "Soy una persona"
# class Estudiante(Persona):
#     def presentarse(self):
#         return"Soy un estudiante"

#ENCAPSULAMIENTO
#Encapsular es controlar cómo se accede y cómo se modifica el estado interno del objeto
# class Estudiante:
#     def__init__(self, nota):
#     self.__nota=nota

#     def mostrar_nota(self):
#         return self.__nota
#atribujo público self.nota, atribujo privado self.__nota


#_atributo y __atributo
#No son exactamente lo mismo, Representan niveles diferentes de proteccción o intención
# _atributo #Uso interno por convención
# __atributo Acceso más restringido, Python aplica name mangling
# Regla rápida, Un guion bajo advierte, Dos guiones restringen más
# class Sensor:
#     def__init__(self):
#     self.ubicación="Sala"
#     self.temperatura=25
# #_ubicación es interno por convención
# #__ubicación

#GETTER Y SETTER
#Son parámetrod para consultar o modificar un atributo de manera controlada
# class Estudiante:
#     def__init__(self, nota):
#     self.__nota=nota
#     def mostrar_nota(self):
#         return self.__nota
#     def cambiar_nota(self,nueva_nota):
#         if 0 <=nueva_nota <= 5:
#             self.__nota=nueva_nota
# #Validar antes de modificar
# estudiante1=Estudiante(4.5)
# print(estudiante1.mostrar_nota())
# estudiante1=Estudiante(3.8)
# print(estudiante1.mostrar_nota())
# estudiante1=Estudiante(7)
# print(estudiante1.mostrar_nota())

##MÉTODO OBTENER_ESTADO()
#El objeto puede decidir su estado usando su propia nota encapsulada

# class Estudiante:
#     def __init__(self,nota):
#     self.__nota=nota
#     def mostrar_nota(self):
#         return self.__nota
#     def cambiar_nota(self,nueva_nota):
#         if 0 <=nueva_nota <= 5:
#             self.__nota=nueva_nota
#     def obtener_estado(self):
#         if self.__nota>=3:
#             return f"Aprobado con:"{self.__nota}:
#         else:
#             return f"Reprobado con"{self.__nota}
#             print(estudiante.obtener_estado())
# #Validar antes de modificar
# estudiante1=Estudiante(4.5)
# print(estudiante1.mostrar_nota())
# estudiante1=Estudiante(3.8)
# print(estudiante1.mostrar_nota())
# estudiante1=Estudiante(7)
# print(estudiante1.mostrar_nota())


#DOS OBJETOS, ESTADOS DIFERENTES]
#Ambos objetos son Estudiante, pero cada uno conerva su propia información
# estudiante1=Estudiante("Luis",34,"Lic. T3ecnología",4.5)
# estudiante2=Estudiante("Pedro",25,"Lic. T3ecnología",2.8)
# print(estudiante1.obtener_estado())
# print(estudiante2.obtener_estado())

#PORQUE ENCAPSULAR 
#Encapsulamos los datos que no deberían modificarse libremente desde cualquier parte del programa
# class Cuenta:
#     def__init__(self,titular,saldo):
#         self.titular=titular
#         self.saldo=saldo
#     def consultar_saldo(slef):
#         return self.__saldo
#     def depositar(self, canridad):
#         if cantidad >0:
#             self.__saldo+=cantidad

#EJERICIO

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera, nota):
        super().__init__(nombre, edad)  # 3. Usar super()
        self.carrera = carrera
        self.__nota = nota  # 4. Encapsulada
        self.cambiar_nota(nota) # Validamos desde el inicio

    def mostrar_nota(self):
        return f"La nota de {self.nombre} es: {self.__nota}"

    def cambiar_nota(self, nueva_nota):
        # Validación de nota (sistema colombiano 0 a 5)
        if 0 <= nueva_nota <= 5:
            self.__nota = nueva_nota
        else:
            print(f"Error: Nota inválida ({nueva_nota}). Debe estar entre 0 y 5.")

    def obtener_estado(self):
        # if self.__nota:
        #     return "Sin nota válida"
        if self.__nota >= 3.0:
            return "Aprobado"
        else:
            return "Reprobado"
    
    # Extra para cumplir bien el presentarse
    def presentarse(self):
        base = super().presentarse()
        return f"{base} Estudio {self.carrera}."

#CPMPRUEBA

# 1. Un estudiante aprobado
est1 = Estudiante("Laura", 20, "Ingeniería", 4.2)
print(est1.presentarse())
print(est1.mostrar_nota())
print(est1.obtener_estado())
print()

# 2. Un estudiante reprobado
est2 = Estudiante("Carlos", 22, "Derecho", 2.5)
print(est2.presentarse())
print(est2.mostrar_nota())
print(est2.obtener_estado())
print()

# 3. Una nota inválida
est3 = Estudiante("Ana", 19, "Medicina", 10) # va a dar error
print(est3.mostrar_nota())
print(est3.obtener_estado())

est1.cambiar_nota(2.5)
print(est1.obtener_estado())

# Probando que no se puede acceder directo a __nota
# print(est1.__nota) -> Esto da error, que es lo que quiere tu profe
    
