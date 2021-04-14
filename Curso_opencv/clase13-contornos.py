import cv2
import numpy as np

imagen1 = cv2.imread('img\Mangekyou.png')
imagen2 = cv2.imread('img\Mangekyou.png',0)
_, th = cv2.threshold(imagen2,100,255,cv2.THRESH_BINARY)

contorno,hierarchy = cv2.findContours(th,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen1,contorno,-1,(0,255,0),3)
'''
for i in range(len(contorno)):
    cv2.drawContours(imagen1,contorno,i,(0,255,0),3)
    cv2.imshow('imagen',imagen1)
    cv2.waitKey(0)
'''
cv2.imshow('th',th)
cv2.imshow('imagen',imagen1)
cv2.waitKey(0)
cv2.destroyAllWindows()