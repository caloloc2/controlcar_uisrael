import time
from gpio import GPIORasp
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('google-services')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://controluisrael-aa34e-default-rtdb.firebaseio.com/'
})

class FirebaseNube:

    def __init__(self):
        self.gpio = GPIORasp()
        return True
    
    def lectura(self):
        while True:
            dato = ''
            hora = ''
            archivo = open("estados.rsp", "r") 
            for linea in archivo.readlines():		
                dato+= linea

            dato = db.reference('bloqueo')

            if (dato=="1"):
                print ("Activa/ Desactiva Bloqueo")
                self.gpio.accion(2, False)
            if (dato=="2"):
                print ("Activa/Desactiva Seguros")
                self.gpio.accion(2, True)

            locacion = db.reference('locacion')

            if (locacion=="1"):
                print ("Activa/ Desactiva Bloqueo")
                self.gpio.accion(3, False)
            if (locacion=="2"):
                print ("Activa/Desactiva Seguros")
                self.gpio.accion(3, True)

            time.sleep(1)