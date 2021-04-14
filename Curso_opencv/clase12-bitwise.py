import cv2
import numpy as np

img1 = np.zeros((400,600),dtype=np.uint8)
img1[100:300,200:400]=255

img2 = np.zeros((400,600),dtype=np.uint8)
img2 = cv2.circle(img2,(300,200),125,(255),-1)

#logica nomas
b_and = cv2.bitwise_and(img1,img2)#px blanco(255) and negro(0) = negro(0); blanco and blanco = blanco
b_or = cv2.bitwise_or(img1,img2)
b_not = cv2.bitwise_not(img1)
b_xor = cv2.bitwise_xor(img1,img2)#00,11 = 0, combinanciones entre 0 y 1 = 1

cv2.imshow('IMG1',img1)
cv2.imshow('IMG2',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()