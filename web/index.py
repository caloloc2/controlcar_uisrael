from flask import Flask, Response, render_template
from libs.camara import Camara
from threading import Thread
from libs.firebase import Firebase
from libs.setup import Setup
from libs.gpio import GPIORasp
import time

llave = GPIORasp(23, 0)

# Inicializa las variables de configuracion
setup = Setup()

camara = Camara()
app = Flask(__name__)

firebase = Firebase()
f = Thread(target = firebase.lectura)
f.daemon = True
f.start()

def switchLlave():
    while True:
        estadoAlarma = llave.read()
        if (estadoAlarma == 0):
            print("Contacto accionado")
            # params = {'valor': 1}
            # self.server.get('alarma.php', params)
        elif (estadoAlarma == 1):
            # params = {'valor': 0}
            # self.server.get('alarma.php', params)
            print("Sin Contacto")
        time.sleep(1)

sw = Thread(target = switchLlave)
sw.daemon = True
sw.start()

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    while True:
        ret, jpeg = camara.reconocimiento()
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2204, threaded=True)
    