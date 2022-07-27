from libs.httpRequest import ServerBridge
from libs.gpio import GPIORasp
import time, os

class Firebase:

    def __init__(self):
        self.server = ServerBridge()
        self.bloqueo = GPIORasp(21)
        self.activacion = GPIORasp(16)
        self.desactivacion = GPIORasp(20)

        self.ahorro = GPIORasp(24, 0)
        self.alarma = GPIORasp(23, 0)
        self.cambioAlarma = False

    def lectura(self):
        while(True):
            data = self.server.get('index.php')
            print(data)
            estadoLed = data['estados']['bloqueo']
            self.bloqueo.accion(estadoLed)

            estadoLed = data['estados']['activacion']
            self.activacion.accion(estadoLed)

            estadoLed = data['estados']['desactivacion']
            self.desactivacion.accion(estadoLed)

            estadoAlarma = self.alarma.read()
            if (estadoAlarma == 0):
                params = {'valor': 1}
                self.server.get('alarma.php', params)
                self.cambioAlarma =  False 
            elif (estadoAlarma == 1):
                if (self.cambioAlarma == False):
                    params = {'valor': 1}
                    self.server.get('alarma.php', params)
                    self.cambioAlarma = True

            apagado = data['estados']['apagado']
            if (apagado == 1):
                os.system("sudo shutdown -h now")
            time.sleep(2)