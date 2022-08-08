# pip install py532lib
import time
from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *
from libs.gpio import GPIORasp
from libs.httpRequest import ServerBridge

class NFCLector:

    def __init__(self):
        self.pn532 = Pn532_i2c()
        self.pn532.SAMconfigure()
        self.naranja = GPIORasp(26)
        self.server = ServerBridge()

    def __convert__(self, byte):
        return int.from_bytes(byte, "big")

    def lectura(self):
        while(True):
            cardData = self.pn532.read_mifare().get_data()
            codigo = self.__convert__(cardData)
            print(codigo)

            if (codigo == 90674177285458846270261753):
                self.naranja.accion(True)
                params = {'valor': 1}
                self.server.get('inicio.php', params)
                time.sleep(5)
                self.naranja.accion(False)
                params = {'valor': 0}
                self.server.get('inicio.php', params)