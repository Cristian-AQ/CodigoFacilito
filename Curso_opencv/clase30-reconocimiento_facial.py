import cv2
import numpy as np
import os
import imutils

personaName = 'isabel'
dataPath = 'caras/'
facePath = dataPath+'caras_video'
#dataPath = 'C:/Users/51927/Desktop/caras'
personaPath = facePath+'/'+personaName

if not os.path.exists(personaName):
    print('Carpeta Creada '+personaName)
    os.mkdir(personaPath)

video = cv2.VideoCapture(dataPath+personaName+'.mp4')

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

#en caso keramo agregar mas imagenes tendriamos que cmbiar el cont
#y realizar el entrenamiento nuevamente

cont = 0

while True:
    ret,frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()

    face = faceClassif.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150))
        cv2.imwrite(personaPath+f'/{cont}.jpg',rostro)
        cont = cont + 1
    
    cv2.imshow('PRUEBA',frame)

    k = cv2.waitKey(1)
    if k == ord('x') or cont>=300:#el cont hace que se almacenen 300 img automaticamente
        break

video.release()
cv2.destroyAllWindows()