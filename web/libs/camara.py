import cv2
import os
from libs.httpRequest import ServerBridge

class Camara:

    def __init__(self):
        self.dataPath = 'Data'
        self.imagePaths = os.listdir(self.dataPath)
        print("[Iniciando camara...]")
        self.video = cv2.VideoCapture(0)
        print("[Iniciando reconocimiento...]")
        self.face_recognizer = cv2.face.EigenFaceRecognizer_create()
        self.face_recognizer = cv2.face.FisherFaceRecognizer_create()
        self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()

        self.face_recognizer.read('modeloLBPHFace.xml')
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        print("[Listo para reconocimiento]")

    def reconocimiento(self):
        while True:
            success, image = self.video.read()
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            auxFrame = gray.copy()
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

            try:
                for (x,y,w,h) in faces:
                    rostro = auxFrame[y:y+h,x:x+w]
                    rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
                    result = self.face_recognizer.predict(rostro)

                    cv2.putText(image,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
                
                    if (len(result) > 0):
                        # LBPHFace
                        if result[1] < 70:
                            cv2.putText(image,'{}'.format(self.imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                            cv2.rectangle(image, (x,y),(x+w,y+h),(0,255,0),2)
                        else:
                            cv2.putText(image,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                            cv2.rectangle(image, (x,y),(x+w,y+h),(0,0,255),2)
            except:
                print("Error")

            return cv2.imencode('.jpg', image)
    
    def captura(self):
