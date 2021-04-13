#Paso1:IMAGEN O VIDEO A PROCESAR
#Paso2:CONVERTIR BGR A HSV
#Paso3:RANGO DE COLORES
#Paso4:VISUALIZACION
#la parte blanca son los colores detectados dentro del rango
import cv2
import numpy as np

video = cv2.VideoCapture(0)

#Rango de colores [H,S,V]
redBajo1 = np.array([0,100,20],np.uint8)
redAlto1 = np.array([8,255,255],np.uint8)

redBajo2 = np.array([175,100,20],np.uint8)
redAlto2 = np.array([179,255,255],np.uint8)

while True:
    ret,frame = video.read()
    if ret == True:
        frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#convertir BGR a HSV
        #lectura de rangos de color
        maskRed1 = cv2.inRange(frameHSV,redBajo1,redAlto1)
        maskRed2 = cv2.inRange(frameHSV,redBajo2,redAlto2)
        #unir mask
        maskRed = cv2.add(maskRed1,maskRed2)
        #mostrara los colores que se encuentra en nuestro rango
        maskRedvis = cv2.bitwise_and(frame,frame,mask=maskRed)

        cv2.imshow('R',maskRedvis)
        cv2.imshow('V',frame)
        cv2.imshow('M',maskRed)
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break
video.release()
cv2.destroyAllWindows()
