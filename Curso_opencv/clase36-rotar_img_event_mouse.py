import cv2
import numpy as np
import imutils

def dibujando(event,x,y,flags,param):
    global angulo,imagen_r
    #boton izquierdo
    if event == cv2.EVENT_LBUTTONDOWN:
        angulo = angulo + 15
        M2 = cv2.getRotationMatrix2D((ancho/2,alto/2),angulo,1)#con el '/2'rotan las aspas
        imagen_r = cv2.warpAffine(imagen,M2,(ancho,alto))
    #boton derecho
    if event == cv2.EVENT_RBUTTONDOWN:
        angulo = angulo - 15
        M2 = cv2.getRotationMatrix2D((ancho/2,alto/2),angulo,1)#con el '/2'rotan las aspas
        imagen_r = cv2.warpAffine(imagen,M2,(ancho,alto))
    
#creacion de una ventana negra
imagen = cv2.imread('img\Mangekyou.png')
imagen_r = imagen.copy()
ancho = imagen.shape[1]#columnas
alto = imagen.shape[0]#filas
angulo = 0 
cv2.namedWindow('ROTACION')
cv2.setMouseCallback('ROTACION', dibujando)#segundo parametro es una funcion

while True:
    cv2.imshow('ROTACION',imagen_r)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('x'):
        break
cv2.destroyAllWindows()