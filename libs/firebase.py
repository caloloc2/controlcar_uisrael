from httpRequest import ServerBridge
from gpio import GPIORasp
import time 

class Firebase:

    def __init__(self):
        self.server = ServerBridge()
        self.rojo = GPIORasp(19)

    def lectura(self):
        while(True):
            data = self.server.get('estado.php')
            print(data)
            estadoLed = data['estado']['puertas']
            self.rojo.accion(estadoLed)
            
            time.sleep(5)

firebase = Firebase()

try:
    firebase.lectura()
except KeyboardInterrupt:
    print("cancelado")