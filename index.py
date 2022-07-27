from libs.gps import GPS
import time
from threading import Thread
from libs.firebase import Firebase
from libs.nfc import NFCLector
from libs.setup import Setup

# Inicializa las variables de configuracion
setup = Setup()

# Inicia servicio de lectura de Firebase para activacicon/desactivacion
firebase = Firebase()
f = Thread(target = firebase.lectura)
f.daemon = True
f.start()

# Inicia servicio de lectura de NFC RFID
nfc = NFCLector()
n = Thread(target = nfc.lectura)
n.daemon = True
n.start()

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
