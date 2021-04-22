import cv2
import numpy as np
import imutils

#ajustar siempre
azulBajo = np.array([95,100,20],np.uint8)
azulAlto = np.array([135,255,255],np.uint8)

imagen = cv2.imread('caras/emotion/molesta.jpg')

#convirtiendo a escala de grises
imgGray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)#la img tiene un canal
#convertir img de un canal a tres canales
imgGray = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR)
imgHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)#la img tiene tres canales

#detectar el color en la img
maskAzul = cv2.inRange(imgHSV, azulBajo, azulAlto)
#mejorar contorno
#maskAzul = cv2.medianBlur(maskAzul,1)
#extrayendo colores
azulDetec = cv2.bitwise_and(imagen, imagen,mask=maskAzul)
#fondo en escala de grises
invMask = cv2.bitwise_not(maskAzul)
bgGray = cv2.bitwise_and(imgGray,imgGray,mask=invMask)
#uniendo bgGray and azulDetec
imgFinal = cv2.add(bgGray,azulDetec)

cv2.imshow('A',imgFinal)
cv2.waitKey(0)
cv2.destroyAllWindows()

