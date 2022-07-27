from libs.httpRequest import ServerBridge
from libs.gpio import GPIORasp
import time 

class Firebase:

    def __init__(self):
        self.server = ServerBridge()
        self.bloqueo = GPIORasp(16)
        self.activacion = GPIORasp(21)

    def lectura(self):
        while(True):
            data = self.server.get('index.php')
            print(data)
            estadoLed = data['estados']['bloqueo']
            self.bloqueo.accion(estadoLed)
            estadoLed = data['estados']['activacion']
            self.activacion.accion(estadoLed)
            time.sleep(2)