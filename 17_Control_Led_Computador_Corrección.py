import serial
from time import sleep

puerto=serial.Serial("COM10", 115200, timeout=3) # se abre el puerto serial, con el nombre del puerto y la velocidad de comunicación

sleep(3) # se espera 3 segundos para que el puerto se abra correctamente

puerto.reset_input_buffer() # se limpia el buffer de entrada del puerto serial, para que no haya datos antiguos

while True: #ciclo infinito
    mensaje=input("Digite ENCENDER o APAGAR para controlar el led: ") # se pide al usuario que digite un mensaje
    puerto.write((mensaje+ "\n").encode()) # se convierte a bytes y se agrega un salto de línea

    respueta= puerto.readline().decode().strip() # se lee la respuesta del ESP32, se convierte a texto y se elimina el salto de línea al final
    print(respueta)

