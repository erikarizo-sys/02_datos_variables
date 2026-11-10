from machine import Pin, time_pulse_us #determina el tiempo que tarda en recibir la señal de retorno del sensor ultrasónico
from time import sleep, sleep_us #importando los pines que se estan utilizando
#ambos trabajan en microsegundos, pero time_pulse_us es mas preciso, y sleep_us es mas rapido

trig=Pin(18, Pin.OUT) #PIN en mayuscula, GPI18, salida digital
echo=Pin(19, Pin.IN) #PIN en mayuscula, GPI19, entrada digital

while True: #ciclo infinito
    trig.value(0) # se pone en 0 el pin de salida, para que no haya señal
    sleep_us(2) # se espera 2 microsegundos, para que el pin de salida se estabilice

    trig.value(1) # se pone en 1 el pin de salida, para que haya señal
    sleep_us(10) # se espera 10 microsegundos, para que el pin de salida se estabilice
    trig.value(0) # se pone en 0 el pin de salida, para que no haya señal

    tiempo= time_pulse_us(echo, 1,30000) # se mide el tiempo que tarda en recibir la señal de retorno del sensor ultrasónico, en microsegundos, y se guarda en la variable tiempo

    if tiempo < 0: # si el tiempo es menor a 0, significa que no se recibió la señal de retorno del sensor ultrasónico
        distance=tiempo/58 # se calcula la distancia en cm, dividiendo el tiempo entre 58, ya que la velocidad del sonido es de 343 m/s, y se multiplica por 100 para convertirlo a cm
        print(round(distance,1)) # se imprime la distancia en cm, redondeada a 1 decimal
    else: # si el tiempo es mayor a 0, significa que se recibió la señal de retorno del sensor ultrasónico
        print("Sin medición válida") # se imprime que la distancia está fuera de rango
    sleep(1) # se espera 1 segundo, para que el sensor ultrasónico se estabilice y no se sature de mediciones