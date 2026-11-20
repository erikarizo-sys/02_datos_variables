import serial
from time import sleep

# Conexión al puerto serie
puerto = serial.Serial("COM10", 115200, timeout=3)
sleep(3)
puerto.reset_input_buffer()

print("Monitoreando distancia desde el ESP32...")

while True:
    dato = puerto.readline().decode().strip()
    if dato:
        try:
            distancia = float(dato)
            print("Distancia medida:", distancia, "cm")
        except ValueError:
            pass