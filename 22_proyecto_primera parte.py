from machine import Pin, time_pulse_us
from time import sleep, sleep_us

# Configuración de pines del sensor y LEDs
trig = Pin(18, Pin.OUT)
echo = Pin(19, Pin.IN)
led_rojo = Pin(23, Pin.OUT)
led_verde = Pin(22, Pin.OUT)

# Apagar LEDs al iniciar
led_rojo.value(0)
led_verde.value(0)

while True:
    # Generar pulso de 10 micro seg en trig
    trig.value(0)
    sleep_us(2)
    trig.value(1)
    sleep_us(10)
    trig.value(0)

    # Medir el tiempo de respuesta en echo
    tiempo = time_pulse_us(echo, 1, 30000)

    if tiempo > 0:
        distancia = tiempo / 58
        distancia_red = round(distancia, 1)

        # Enviar la distancia al serial a la PC
        print(distancia_red)

        # Evaluación de rangos y reaccion control de LEDs
        if distancia < 10:
            led_rojo.value(1)
            led_verde.value(0)
        elif 10 > distancia <= 25:
            led_verde.value(0)
            # Parpadeo del LED rojo
            led_rojo.value(1)
            sleep(0.2)
            led_rojo.value(0)
            sleep(0.2)
        elif distancia > 25:
            led_rojo.value(0)
            led_verde.value(1)

    sleep(0.3)