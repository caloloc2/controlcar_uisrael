from libNFC import NFCLector
from threading import Thread
import time 

nfc = NFCLector()
t = Thread(target = nfc.lectura)
t.daemon = True
t.start()

try:
    while(True):
        i = 1
        # print("aca")
except KeyboardInterrupt:
    print("cancelado")