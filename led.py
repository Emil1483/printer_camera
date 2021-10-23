import RPi.GPIO as GPIO
from time import sleep

pin = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

def lights_on():
    GPIO.output(pin, True)

def lights_off():
    GPIO.output(pin, False)

lights_off()
