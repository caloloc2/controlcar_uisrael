import time
import serial
from libs.httpRequest import ServerBridge

class GPS:

    def __init__(self, module = "$GPRMC,"):
        print("[INFO] GPS conectado y leyendo información de ubicación.")
        self.gpsModule = serial.Serial("/dev/serial0")
        self.module = module
        self.internet = ServerBridge()
        self.contador = 30

    def __calculoPosition(self, pos = 0):
        try:
            if (pos != ''):
                decimal = float(pos) / 100.00
                degrees  = int(decimal)
                mm = (decimal - degrees) / 0.6
                position = (degrees + mm) * - 1
                return position
        except:
            return 0
    
    def __kph(self, knots):
        try:
            if (knots != ''):
                  return float(knots) * 1.852
        except:
            return 0
      
    def __explodeData(self, data):
        latitude = None 
        longitude = None
        velocity = None
        gpsDate = None 
        gpsTime = None 
        try:
            GPGGA_data_available = data.find(self.module)
            if (GPGGA_data_available>0):
                GPGGA_buffer = data.split(self.module, 1)[1]
                NMEA_buff = (GPGGA_buffer.split(','))
                gpsTime = NMEA_buff[0]
                latitude = self.__calculoPosition(NMEA_buff[2])
                longitude = self.__calculoPosition(NMEA_buff[4])
                velocity = self.__kph(NMEA_buff[6])
                gpsDate = NMEA_buff[8]
        except:
            print("-")
        
        return [latitude, longitude, velocity, gpsDate, gpsTime]

    def readPosition(self):
        try:
            i = 0
            while True:
                received_data = (str)(self.gpsModule.readline())
                linea = self.__explodeData(received_data)
                if (linea != None):
                    print(linea)
                    i += 1
                    if (i >= self.contador):
                        params = {'lng': linea[0], 'lat': linea[1]}
                        self.internet.get('ubicacion.php', params)
                        i = 0
        except KeyboardInterrupt:
            print("Cancelado")
        except:
            print("El dispositivo GPS no puede ser leido por el puerto. Revise conexión y reinicie.")
            self.gpsModule = serial.Serial("/dev/serial0")