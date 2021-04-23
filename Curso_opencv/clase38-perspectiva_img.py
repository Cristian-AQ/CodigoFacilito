import cv2
import numpy as np

def redimension(event,x,y,flags,param):
    global puntos
    if event == cv2.EVENT_LBUTTONDOWN:
        #cv2.circle(img, (x,y), 5, (0,255,0),2)
        puntos.append([x,y])

puntos = []
img = cv2.imread('caras/emotion/sonrisa.jpg')
imgAux = img.copy()#necesario para limpiar la img
cv2.namedWindow('A')
cv2.setMouseCallback('A', redimension)

while True:
    if len(puntos) == 4:#cantidad de elementos en la lista
        pto1 = np.float32([puntos])
        pto2 = np.float32([[0,0],[480,0],[0,300],[480,300]])#tamaño de la ventana que se mostrara la img

        #matriz de transformacion   
        M = cv2.getPerspectiveTransform(pto1, pto2)
        dst = cv2.warpPerspective(img, M, (480,300))
        cv2.imshow('B',dst)

    cv2.imshow('A', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('x'):
        break
    if k == ord('s'):
        img = imgAux.copy()
        puntos = []

cv2.destroyAllWindows()