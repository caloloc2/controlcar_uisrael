from libs.gps import GPS
import time
from threading import Thread
import os

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
