import time
import serial

class GPS:

    def __init__(self, module = "$GPRMC,"):
        self.gpsModule = serial.Serial("/dev/serial0")
        self.module = module

    def __calculoPosition(self, pos = 0):
        decimal = float(pos) / 100.00
        degrees  = int(decimal)
        mm = (decimal - degrees) / 0.6
        position = (degrees + mm) * - 1
        return position
    
    def __kph(self, knots):
        return float(knots) * 1.852
    
    def __explodeData(self, data):
        GPGGA_data_available = data.find(self.module)
        if (GPGGA_data_available>0):
            GPGGA_buffer = data.split(self.module, 1)[1]
            NMEA_buff = (GPGGA_buffer.split(','))
            gpsTime = NMEA_buff[0]
            latitude = self.__calculoPosition(NMEA_buff[2])
            longitude = self.__calculoPosition(NMEA_buff[4])
            velocity = self.__kph(NMEA_buff[6])
            gpsDate = NMEA_buff[8]
            return [latitude, longitude, velocity, gpsDate, gpsTime]

    def readPosition(self):
        try:
            while True:
                received_data = (str)(self.gpsModule.readline())
                linea = self.__explodeData(received_data)
                if (linea != None):
                    print(linea, linea[1])
                # time.sleep(10)
        except KeyboardInterrupt:
            print("Cancelado")