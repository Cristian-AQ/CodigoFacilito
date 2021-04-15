import cv2
import numpy as np
import imutils

imagen = cv2.imread('img\Mangekyou.png')
ancho = imagen.shape[1]#columnas
alto = imagen.shape[0]#filas

#TRASLACION
M1 = np.float32([[1,0,10],[0,1,100]])#10,100 son respectivamente x,y
salida1 = cv2.warpAffine(imagen,M1,(ancho,alto))#aplica la transformacion a una imagen
                                    #M es matriz de transformacion
#ROTACION DE IMAGEN CON TECLADO
for i in range(360):
    #ROTACION
    M2 = cv2.getRotationMatrix2D((ancho/2,alto/2),i,1)#con el '/2'rotan las aspas
    salida2 = cv2.warpAffine(imagen,M2,(ancho,alto))
    cv2.imshow('SALIDA2',salida2)
    cv2.waitKey(0)

#ESCALADO-RECOMENDADO IMULTIS(se ingresa una medida, se calcula la segunda)
salida3 = imutils.resize(imagen,width=600)

#RECORTE
salida4 = imagen[150:300,200:400]#[f_inicial:f_final,c_inicial:c_final]
cv2.imshow('ENTRADA',imagen)
cv2.imshow('SALIDA1',salida1)
cv2.imshow('SALIDA3',salida3)
cv2.waitKey(0)
cv2.destroyAllWindows()