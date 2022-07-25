# import os
# import sys
# lib_path = os.path.abspath('../../')
# sys.path.append(lib_path)

from libs.nfclib.i2c import *
from libs.nfclib.frame import *
from libs.nfclib.constants import *

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