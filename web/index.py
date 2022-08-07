from ast import Not
from glob import glob
from re import A
from flask import Flask, Response, render_template
from libs.camara import Camara
from threading import Thread
from libs.firebase import Firebase
from libs.setup import Setup
from libs.gpio import GPIORasp
from libs.httpRequest import ServerBridge
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

firebase = Firebase()
f = Thread(target = firebase.lectura)
f.daemon = True
f.start()

servidor = ServerBridge()
def revision():
    global servidor
    global nuevoUsuario
    while (True):
        data = servidor.get('anadirUsuario.php')
        if (data['estado']):
            camara.setEstado(2, data['nombre'])
            nuevoUsuario = True 
        
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
    while True:
        imagen, reconocido, usuario = camara.reconocimiento()
        if (reconocido and bloqueoActivado and nuevoUsuario == False):
            print("[INFO] Se ha activado el automovil.")
            bloqueoActivado = False 
            camara.setEstado(0)
            bloqueo.accion(False)
        
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
    