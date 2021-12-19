import RPi.GPIO as GPIO
from timer import ResettableTimer

pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

def lights_off():
    GPIO.output(pin, False)

timer = ResettableTimer(10, lights_off)

def lights_on():
    GPIO.output(pin, True)
    timer.reset()

lights_off()
