from httpRequest import ServerBridge
from gpio import GPIORasp
import time 

class Firebase:

    def __init__(self):
        self.server = ServerBridge()
        self.bloqueo = GPIORasp(19)
        self.activacion = GPIORasp(21)

    def lectura(self):
        while(True):
            data = self.server.get('index.php')
            print(data)
            estadoLed = data['estados']['bloqueo']
            self.bloqueo.accion(estadoLed)
            estadoLed = data['estados']['activacion']
            self.activacion.accion(estadoLed)
            time.sleep(5)

firebase = Firebase()

try:
    firebase.lectura()
except KeyboardInterrupt:
    print("cancelado")