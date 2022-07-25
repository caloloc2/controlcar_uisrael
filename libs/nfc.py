# import sys
# sys.path.insert(0, '../')

from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *

class NFCLector:

    def __init__(self):
        self.pn532 = Pn532_i2c()
        self.pn532.SAMconfigure()

    def __convert__(self, byte):
        return int.from_bytes(byte, "big")

    def lectura(self):
        while(True):
            cardData = self.pn532.read_mifare().get_data()
            print(self.__convert__(cardData))      