import cv2
import os
import shutil

if not os.path.exists('Rostros Encontrados'):
    print('Carpeta creada: Rostros Encontrados')
    os.mkdir('C:/Users/51927/Desktop/Rostros Encontrados')#especificar ruta y nombre de la carpeta, por defecto se crea en la ubicacion del Script

video = cv2.VideoCapture(0)

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

cont = 0

while True:
    ret,frame = video.read()
    frame = cv2.flip(frame,1)
    gris = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()

    face = faceClassif.detectMultiScale(gris,1.3,5)
    k = cv2.waitKey(1)
    if k == ord('x'):
        break
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(60,60))
        if k == ord('s'):
            cv2.imwrite(f'C:/Users/51927/Desktop/Rostros Encontrados/captura{cont}.jpg',rostro)
            cv2.imshow('ROSTRO',rostro)
            cont = cont + 1
    cv2.rectangle(frame,(10,5),(450,25),(255,255,255),-1)
    mensaje1 = 'Presione \'s\' para guardar los rostros encontrados'
    cv2.putText(frame,mensaje1,(10,20),2,0.5,(128,0,255),1,cv2.LINE_AA)

    cv2.rectangle(frame,(10,365),(230,385),(255,255,255),-1)
    mensaje2 = 'Presione \'x\' para salir'
    cv2.putText(frame,mensaje2,(10,380),2,0.5,(128,0,255),1,cv2.LINE_AA)
    cv2.imshow('VIDEO',frame)
video.release()
cv2.destroyAllWindows()    