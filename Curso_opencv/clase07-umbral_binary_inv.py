import cv2
import numpy as np
import imutils

imagen = cv2.imread('img\Hiromi Maiharu.jpg',0)
imagen = imutils.resize(imagen,width=400)#especificar tamaño imagen

_, binary = cv2.threshold(imagen,100,255,cv2.THRESH_BINARY)
_, binary_inv = cv2.threshold(imagen,100,255,cv2.THRESH_BINARY_INV)


cv2.imshow('M',imagen)
cv2.imshow('NORMAL-INVERTIDO',np.hstack([binary,binary_inv]))
cv2.waitKey(0)
cv2.destroyAllWindows()