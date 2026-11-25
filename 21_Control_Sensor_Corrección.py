import serial
from time import sleep

puerto= serial.Serial("COM10", 115200, timeout=3) # se abre el puerto serial, con el nombre del puerto y la velocidad de comunicación
sleep(3) # se espera 3 segundos para que el puerto se abra correctamente
puerto.reset_input_buffer() # se limpia el buffer de entrada del puerto serial, para que no haya datos antiguos

while True: #ciclo infinito
    dato=puerto.readline().decode().strip() # se lee la respuesta del ESP32, se convierte a texto y se elimina el salto de línea al final

    try: # se intenta convertir el dato a número decimal
        distancia= float(dato) # se convierte a número decimal
        print("Distancia: ", distancia, "cm") # se imprime la distancia medida por el sensor ultrasónico

        if distancia < 10: # si la distancia es menor a 10 cm
            puerto.write(b"ENCENDER\n") # se convierte a bytes y se agrega un salto de línea
        else: # si la distancia es mayor o igual a 10 cm
            puerto.write(b"APAGAR\n") # se convierte a bytes y se agrega un salto de línea

    except ValueError: # si el dato no se puede convertir a número decimal
        pass # se ignora el dato y se continúa con el siguiente ciclo