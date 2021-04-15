import cv2
import imutils

imagen1 = cv2.imread('img\poligonos.png')
imagen1 = imutils.resize(imagen1,width=600)

imagen2 = cv2.imread('img\poligonos.png',0)
imagen2 = imutils.resize(imagen2,width=600)
borde = cv2.Canny(imagen2,50,100)#deteccion de bordes

contorno,_=cv2.findContours(borde,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen1,contorno,-1,(0,255,0),3,cv2.LINE_AA)

mensaje = f'HAY EN TOTAL {len(contorno)} POLIGONOS'
cv2.putText(imagen1,mensaje,(25,35),6,0.7,(0,0,255),1,cv2.LINE_AA)
cv2.imshow('POLIGONOS',imagen1)
cv2.waitKey(0)
cv2.destroyAllWindows()
