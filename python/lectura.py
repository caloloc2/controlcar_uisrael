#!/usr/bin/python
import RPi.GPIO as GPIO
import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('google-services')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://controluisrael-aa34e-default-rtdb.firebaseio.com/'
})

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT) ## GPIO 2 como salida
GPIO.setup(3, GPIO.OUT) ## GPIO 3 como salida
GPIO.setup(4, GPIO.OUT) ## GPIO 4 como salida
GPIO.setup(17, GPIO.OUT) ## GPIO 17 como salida

def lectura():
	dato = ''
	hora = ''
	archivo = open("estados.rsp", "r") 
	for linea in archivo.readlines():		
		dato+= linea

	dato = db.reference('bloqueo')

	if (dato=="1"):
		print ("Activa/ Desactiva Bloqueo")
		GPIO.output(2, False) ## Enciendo el 2
	if (dato=="2"):
		print ("Activa/Desactiva Seguros")
		GPIO.output(2, True) ## Enciendo el 2

	locacion = db.reference('locacion')

	if (locacion=="1"):
		print ("Activa/ Desactiva Bloqueo")
		GPIO.output(2, False) ## Enciendo el 2
	if (locacion=="2"):
		print ("Activa/Desactiva Seguros")
		GPIO.output(2, True) ## Enciendo el 2

while(1):
	lectura()
	time.sleep(0.1)

	#GPIO.cleanup() ## Hago una limpieza de los GPIO