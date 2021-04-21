import cv2
import os

#dataPath = 'C:/Users/51927/Desktop/caras/caras_video'
dataPath = 'caras/caras_video'
peopleList = os.listdir(dataPath)
print(peopleList)

#modelos
face_recognizer = cv2.face.EigenFaceRecognizer_create()
face_recognizer = cv2.face.FisherFaceRecognizer_create()
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

#leemos el archivo xml o yaml que creamos de acorde al modelo utilizado
face_recognizer.read('caras/modelos/modeloFace.xml')

#video = cv2.VideoCapture('C:/Users/51927/Desktop/caras/nicole.mp4')
video = cv2.VideoCapture('caras/isabel.mp4')


faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

while True:
    ret,frame = video.read()
    if ret == False: break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    face = faceClassif.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in face:
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
        #agregamos predict y colocamos el rostro que vamos a identificar
        #ademas brinda coordenadas para realizar una mejor identificacion
        result = face_recognizer.predict(rostro)

        cv2.putText(frame,f'{result}',(x,y+5),1,1.3,(255,255,0),1,cv2.LINE_AA)

        #ajustar de acorde a lo mostrado por result
        if result[1]<4000:
            cv2.putText(frame,f'{peopleList[result[0]]}',(x,y+25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        else:
            cv2.putText(frame,'Desconocido',(x,y+20),2,1.1,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
    
    cv2.imshow('PRUEBA',frame)

    k = cv2.waitKey(1)
    if k == ord('x'):
        break

video.release()
cv2.destroyAllWindows()