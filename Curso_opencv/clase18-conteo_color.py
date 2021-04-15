import cv2
import numpy as np
import imutils

def dibujar_contorno(contorno,color):
    for (i,c) in enumerate(contorno):
        M = cv2.moments(c)
        if (M['m00']==0):
            M['m00'] = 1
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
        cv2.drawContours(imagen,[c],-1,color,2,cv2.LINE_AA)
        cv2.putText(imagen,str(i+1),(x,y),0,0.5,0,2)

redBajo1 = np.array([0,100,20],np.uint8)
redAlto1 = np.array([8,255,255],np.uint8)

redBajo2 = np.array([175,100,20],np.uint8)
redAlto2 = np.array([179,255,255],np.uint8)

azulBajo = np.array([100,100,20],np.uint8)
azulAlto = np.array([125,255,255],np.uint8)

amarilloBajo = np.array([25,100,20],np.uint8)
amarilloAlto = np.array([45,255,255],np.uint8)

verdeBajo = np.array([36,100,20],np.uint8)
verdeAlto = np.array([70,255,255],np.uint8)

naranjaBajo = np.array([9,100,20],np.uint8)
naranjaAlto = np.array([20,255,255],np.uint8)

imagen = cv2.imread('img\colores.jpg')
imagen = imutils.resize(imagen,width=700)
imgHSV = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)

maskAzul = cv2.inRange(imgHSV,azulBajo,azulAlto)
maskAmarillo = cv2.inRange(imgHSV,amarilloBajo,amarilloAlto)
maskVerde = cv2.inRange(imgHSV,verdeBajo,verdeAlto)
maskNaranja = cv2.inRange(imgHSV,naranjaBajo,naranjaAlto)
maskR1 = cv2.inRange(imgHSV,redBajo1,redAlto1)
maskR2 = cv2.inRange(imgHSV,redBajo2,redAlto2)
maskRojo = cv2.add(maskR1,maskR2)

cntAzul,_ = cv2.findContours(maskAzul,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
dibujar_contorno(cntAzul,(255,0,0))

cntAmarillo,_ = cv2.findContours(maskAmarillo,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
dibujar_contorno(cntAmarillo,(0,255,255))

cntVerde,_ = cv2.findContours(maskVerde,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
dibujar_contorno(cntVerde,(0,255,0))

cntNaranja,_ = cv2.findContours(maskNaranja,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
dibujar_contorno(cntNaranja,(17,70,244))

cntRojo,_ = cv2.findContours(maskRojo,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
dibujar_contorno(cntRojo,(0,0,255))

imgResumen = 255*np.ones((210,100,3),np.uint8)#imagen en blanco
cv2.circle(imgResumen,(30,30),10,(255,0,0),-1)
cv2.circle(imgResumen,(30,70),10,(0,255,255),-1)
cv2.circle(imgResumen,(30,110),10,(0,255,0),-1)
cv2.circle(imgResumen,(30,150),10,(17,70,244),-1)
cv2.circle(imgResumen,(30,190),10,(0,0,255),-1)

cv2.putText(imgResumen,f'{len(cntAzul)}',(50,35),5,1,0,2)
cv2.putText(imgResumen,f'{len(cntAmarillo)}',(50,75),5,1,0,2)
cv2.putText(imgResumen,f'{len(cntVerde)}',(50,115),5,1,0,2)
cv2.putText(imgResumen,f'{len(cntNaranja)}',(50,155),5,1,0,2)
cv2.putText(imgResumen,f'{len(cntRojo)}',(50,195),5,1,0,2)

cv2.imshow('COLOR1',imagen)
cv2.imshow('RESUMEN',imgResumen)
cv2.waitKey(0)
cv2.destroyAllWindows()