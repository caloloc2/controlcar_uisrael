#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT) ## GPIO 2 como salida
GPIO.setup(3, GPIO.OUT) ## GPIO 3 como salida
GPIO.setup(4, GPIO.OUT) ## GPIO 4 como salida
GPIO.setup(17, GPIO.OUT) ## GPIO 17 como salida

class GPIORasp:

    def __init__(self):
        return True
 
    def accion(self, pin, state = False):
        GPIO.output(pin, state) ## Enciendo/Apago pin

    def cancel(self):
        GPIO.cleanup()