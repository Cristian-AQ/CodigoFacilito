import cv2
import numpy as np

def dibujando(event,x,y,flags,param):
    #boton izquierdo
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagen, (x,y), 20, (255,255,255),2)
    #boton derecho
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(imagen, (x,y), 20, (0,0,255),2)
    #doble click izquierdo
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(imagen, (x,y), 20, (255,255,255),-1)
    #doble click derecho
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(imagen, (x,y), 20, (0,0,255),-1)
    #el mensaje aparecera en el lugar que dejes de presionar el boton
    #suelta boton izquierdo
    if event == cv2.EVENT_LBUTTONUP:
        cv2.putText(imagen, 'solto el boton izq', (x,y-25), 0, 0.6, (255,255,255),1,cv2.LINE_AA)
    #suelta boton derecho
    if event == cv2.EVENT_RBUTTONUP:
        cv2.putText(imagen, 'solto el boton der', (x,y-25), 0, 0.6, (0,0,255),1,cv2.LINE_AA)

#creacion de una ventana negra
imagen = np.zeros((480,640,3),np.uint8)
cv2.namedWindow('A')
cv2.setMouseCallback('A', dibujando)#segundo parametro es una funcion

while True:
    cv2.imshow('A', imagen)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('x'):
        break
    #limpiar pantalla
    if k == ord('a'):
        imagen = np.zeros((480,640,3),np.uint8)
cv2.destroyAllWindows()