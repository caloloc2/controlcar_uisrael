from ast import Not
from glob import glob
from os import getloadavg
from pickle import GLOBAL
from re import A
from flask import Flask, Response, render_template
from libs.camara import Camara
from threading import Thread
from libs.firebase import Firebase
from libs.setup import Setup
from libs.gpio import GPIORasp
from libs.httpRequest import ServerBridge
from libs.gps import GPS
from libs.nfc import NFCLector
import time

bloqueo = GPIORasp(21)
llave = GPIORasp(23, 0)

# Activa el bloqueo
bloqueo.accion(True)
bloqueoActivado = True
nuevoUsuario = False
print("[INFO] Bloqueo activado automaticamente.")

# Inicializa las variables de configuracion
setup = Setup()

camara = Camara()
app = Flask(__name__)

# Inicia servicio de GPS
gps = GPS()
t = Thread(target = gps.readPosition)
t.daemon = True
t.start()

firebase = Firebase()
f = Thread(target = firebase.lectura)
f.daemon = True
f.start()

# Inicia servicio de lectura de NFC RFID
nfc = NFCLector()
n = Thread(target = nfc.lectura)
n.daemon = True
n.start()

servidor = ServerBridge()
params = {'info': ""}
servidor.get('estadoReconocimiento.php', params)
def revision():
    global servidor
    global nuevoUsuario
    global bloqueoActivado
    while (True):
        data = servidor.get('anadirUsuario.php')
        if (data['estado']):
            camara.setEstado(2, data['nombre'])
            nuevoUsuario = True
        elif(data['entrena']):
            camara.entrenamiento()
            bloqueoActivado = True
            nuevoUsuario = False
        
        time.sleep(1)

sv = Thread(target = revision)
sv.daemon = True
sv.start()

def switchLlave():
    global servidor
    global nuevoUsuario
    while (bloqueoActivado and nuevoUsuario == False):
        estadoAlarma = llave.read()
        if (estadoAlarma == 0):
            camara.setEstado(1)
            params = {'valor': 1}
            servidor.get('alarma.php', params)
        elif (estadoAlarma == 1):
            camara.setEstado(0)
            params = {'valor': 0}
            servidor.get('alarma.php', params)
        time.sleep(1.5)

sw = Thread(target = switchLlave)
sw.daemon = True
sw.start()

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    global bloqueoActivado
    global nuevoUsuario
    global servidor

    contador = 0
    while True:
        imagen, reconocido, usuario, nombreUsuario = camara.reconocimiento()
        if (reconocido and bloqueoActivado and nuevoUsuario == False):
            if (contador >= 50):
                print("[INFO] Se ha activado el automovil.")
                params = {'info': nombreUsuario+ " ha activado el automovil."}
                servidor.get('estadoReconocimiento.php', params)
                bloqueoActivado = False 
                camara.setEstado(0)
                bloqueo.accion(False)
                contador = 0
            contador+=1
        
        if (nuevoUsuario and usuario == False):
            print('[INFO] Termina toma de perfil de usuario.')
            nuevoUsuario = False 
            camara.setEstado(0)

        ret, jpeg = imagen
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2204, threaded=True)
    