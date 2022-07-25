#!/usr/bin/python
import RPi.GPIO as GPIO
import time

class GPIORasp:

    def __init__(self, pin):
        self.pin = pin 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.setwarnings(False)
 
    def accion(self, state = False):
        GPIO.output(self.pin, state) ## Enciendo/Apago pin

    def cancel(self):
        GPIO.cleanup()