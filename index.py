from libs.gps import GPS
import time
from threading import Thread
from libs.firebase import Firebase

# Inicia servicio de lectura de Firebase para activacicon/desactivacion
firebase = Firebase()
f = Thread(target = firebase.lectura)
f.daemon = True
f.start()


# Inicia servicio de GPS
gps = GPS()
t = Thread(target = gps.readPosition)
t.daemon = True
t.start()

try:
    while True:
        time.sleep(0.002)
except KeyboardInterrupt:
    print("cancelado")
