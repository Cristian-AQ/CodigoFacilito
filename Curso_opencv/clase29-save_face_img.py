import cv2
import numpy
import imutils

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

imagen = cv2.imread('img\oficina.png')
imagenAux = imagen.copy()
gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

face = faceClassif.detectMultiScale(gris,1.1,5)

cont = 0

for (x,y,w,h) in face:#remarca cada vez q se teclea
    cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,255,0),2)
    rostro = imagenAux[y:y+h,x:x+w]#recortando rostro
    rostro = imutils.resize(rostro,width=60)
    cv2.imwrite(f'img\captura{cont}.jpg',rostro)#guardar rostro
    cont = cont + 1
    cv2.imshow('rostro',rostro)
    cv2.imshow('A',imagen)
    cv2.waitKey(0)

cv2.destroyAllWindows()