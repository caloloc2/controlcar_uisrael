#!/usr/bin/python
import RPi.GPIO as GPIO
import time

class GPIORasp:

    def __init__(self, pin, mode = 1):
        self.pin = pin 
        GPIO.setmode(GPIO.BCM)
        if (mode == 1):
            GPIO.setup(self.pin, GPIO.OUT)
        elif (mode == 0):
            GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setwarnings(False)
 
    def accion(self, state = False):
        GPIO.output(self.pin, state) ## Enciendo/Apago pin
    
    def read(self):
        return GPIO.input(self.pin)

    def cancel(self):
        GPIO.cleanup()