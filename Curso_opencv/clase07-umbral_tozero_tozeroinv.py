import cv2
import numpy as np
import imutils

imagen = cv2.imread('img\Hiromi Maiharu.jpg',0)
imagen = imutils.resize(imagen,width=600)

#cuando supera el umbral mantiene el color original, caso contrario toma negro(normal,inv(blanco))
_, zero = cv2.threshold(imagen,100,255,cv2.THRESH_TOZERO)
_,zero_inv = cv2.threshold(imagen,100,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('M',imagen)
cv2.imshow('TOZERO-TOZERO_INV',np.hstack([zero,zero_inv]))
cv2.waitKey(0)
cv2.destroyAllWindows()