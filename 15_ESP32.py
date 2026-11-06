# #USAR ENCODE
# #PySerial envía bytes, por eso se convierte el texto antes de enviarlo


# puerto.write((mensaje+ "\n").encode()) # se convierte a bytes y se agrega un salto de línea
# #el salto de linea determina cuando termina el mensaje para que el ESP32 lo reciba correctamente

# "ENCENDER\n"
# "APAGAR\n"

# readline(), espera y lee una linea recibida por el puerto serial, hasta que encuentra un salto de línea. Devuelve los bytes recibidos, incluyendo el salto de línea al final.
# dato=puerto.readline() # lee hasta el salto de línea

# #DECODE,eviar bytes, por eso se convierte a texto antes de mostrarlo

# dato=temperatura.readline() # lee hasta el salto de línea
# dato=dato.decode() # se convierte a texto

# #PREPARAR EL DATO PARA UTILIZARLO
# dato=puerto.readline().decode().strip() # se elimina el salto de línea al final
# temperatura= float(dato) # se convierte a número decimal

from machine import Pin
from time import sleep #importando los pines que se estan utilizando

led = Pin(18, Pin.OUT) #PIN en mayuscula, GPIO18, salida digital

while True: #ciclo infinito
    led.value(1) # enciende el led
    sleep(1) #sleep es delay

    led.value(0) # apaga el led
    sleep(1) #sleep es una pausa de 1 segundo, para que el led se vea encendido y apagado

    
    
