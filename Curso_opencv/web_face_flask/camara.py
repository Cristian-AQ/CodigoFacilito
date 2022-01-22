import cv2
import os

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

class videoCamara(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.cont = 0
        self.raiz = 'web_face_flask/Rostros Encontrados/'
        self.modelo = 'web_face_flask/modelo/modeloFace.xml'
        self.peopleList = os.listdir(self.raiz)
        self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.face_recognizer.read(self.modelo)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        ret,frame = self.video.read()
        frame = cv2.flip(frame,1)
        gris = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face = faceClassif.detectMultiScale(gris,1.1,5)        
        for (x,y,w,h) in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            break
        (flag,encodedImage) = cv2.imencode(".jpg",frame)
        return encodedImage.tobytes()
    
    def frame_capture(self,name,personaPath):
        ret,frame = self.video.read()
        frame = cv2.flip(frame,1)
        gris = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()
        face = faceClassif.detectMultiScale(gris,1.1,5)        
        while(self.cont<200):
            for (x,y,w,h) in face:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                rostro = auxFrame[y:y+h,x:x+w]
                rostro = cv2.resize(rostro,(150,150))
                cv2.imwrite(personaPath+f'/{name}_{self.cont}.jpg',rostro)
                self.cont = self.cont + 1
                break
                
        (flag,encodedImage) = cv2.imencode(".jpg",frame)
        return encodedImage.tobytes()
    
    def detected_face(self):
        ret,frame = self.video.read()
        frame = cv2.flip(frame,1)
        gris = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        auxFrame = gris.copy()
        face = faceClassif.detectMultiScale(gris,1.1,5)        
        for (x,y,w,h) in face:
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
            result = self.face_recognizer.predict(rostro)
            cv2.putText(frame,f'{result}',(x,y+5),1,1.3,(255,255,0),1,cv2.LINE_AA)
            if result[1]<70:
                cv2.putText(frame,f'{self.peopleList[result[0]]}',(x,y+25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
            else:
                cv2.putText(frame,'Desconocido',(x,y+20),2,1.1,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
            break
        (flag,encodedImage) = cv2.imencode(".jpg",frame)
        return encodedImage.tobytes()