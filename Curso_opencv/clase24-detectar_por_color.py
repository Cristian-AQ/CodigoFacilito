import cv2
import numpy as np

def figColor(imagenHSV):
    redBajo1 = np.array([0,100,20],np.uint8)
    redAlto1 = np.array([8,255,255],np.uint8)

    redBajo2 = np.array([175,100,20],np.uint8)
    redAlto2 = np.array([179,255,255],np.uint8)

    celeBajo = np.array([85,100,20],np.uint8)
    celeAlto = np.array([95,255,255],np.uint8)

    amarilloBajo = np.array([25,100,20],np.uint8)
    amarilloAlto = np.array([45,255,255],np.uint8)

    verdeBajo = np.array([36,100,20],np.uint8)
    verdeAlto = np.array([70,255,255],np.uint8)

    maskCele = cv2.inRange(imagenHSV,celeBajo,celeAlto)
    maskAmarillo = cv2.inRange(imagenHSV,amarilloBajo,amarilloAlto)
    maskVerde = cv2.inRange(imagenHSV,verdeBajo,verdeAlto)
    maskR1 = cv2.inRange(imagenHSV,redBajo1,redAlto1)
    maskR2 = cv2.inRange(imagenHSV,redBajo2,redAlto2)
    maskRojo = cv2.add(maskR1,maskR2)

    cntCele,_ = cv2.findContours(maskCele,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cntAmarillo,_ = cv2.findContours(maskAmarillo,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cntVerde,_ = cv2.findContours(maskVerde,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
    cntRojo,_ = cv2.findContours(maskRojo,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    if len(cntRojo)>0: 
        color = 'ROJO' 
    elif len(cntCele)>0: 
        color = 'CELESTE'
    elif len(cntAmarillo)>0: 
        color = 'AMARILLO'
    elif len(cntVerde)>0: 
        color = 'VERDE'
    
    return color

def figName(contorno,width,height):
    epsilon = 0.008*cv2.arcLength(contorno,True)
    aprox = cv2.approxPolyDP(contorno,epsilon,True)

    if len(aprox) == 3:
        namefig = 'TRIANGULO'
    if len(aprox) == 4:
        aspec_radio = float(width)/height
        if aspec_radio == 1:
            namefig = 'CUADRADO'
        else:
            namefig = 'RECTANGULO'
    if len(aprox) == 5:
        namefig ='PENTAGONO'
    if len(aprox) == 6:
        namefig ='HEXAGONO'
    if len(aprox) > 10:
        namefig = 'CIRCULO'
    
    return namefig

imagen = cv2.imread('img\mvariado.jpg')
gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gris,10,150)#deteccion de bordes
canny = cv2.dilate(canny,None,iterations=1)#transformaciones morfologicas
canny = cv2.erode(canny,None,iterations=1)#transformaciones morfologicas

cnt,_ = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
imagenHSV = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)

for c in cnt:
    x,y,w,h = cv2.boundingRect(c)#obtener los puntos del contorno
    imAux = np.zeros(imagen.shape[:2],dtype='uint8')
    imAux = cv2.drawContours(imAux,[c],-1,255,-1)
    maskHSV = cv2.bitwise_and(imagenHSV,imagenHSV,mask=imAux)#presentar img en hsv por figura
    name = figName(c,w,h)
    color = figColor(maskHSV)
    nameColor = name+' '+color
    cv2.putText(imagen,nameColor,(x,y+5),1,1,(0,255,0),2)
    cv2.imshow('DETECTOR',imagen)
    cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()