import cv2
import numpy as np

def redimension(event,x,y,flags,param):
    global puntos
    if event == cv2.EVENT_LBUTTONDOWN:
        puntos.append([x,y])

def dib_punto(puntos):
    for x,y in puntos:
        cv2.circle(frame, (x,y), 5, (0,255,0),2)
puntos = []
video = cv2.VideoCapture('caras/diablito.mp4')
cv2.namedWindow('A')
cv2.setMouseCallback('A', redimension)

while True:
    ret,frame = video.read()
    if ret == False: break
    dib_punto(puntos)
    if len(puntos) == 4:#cantidad de elementos en la lista
        pto1 = np.float32([puntos])
        pto2 = np.float32([[0,0],[480,0],[0,300],[480,300]])#tamaño de la ventana que se mostrara la img

        #matriz de transformacion   
        M = cv2.getPerspectiveTransform(pto1, pto2)
        dst = cv2.warpPerspective(frame, M, (480,300))
        cv2.imshow('B',dst)

    cv2.imshow('A', frame)
    k = cv2.waitKey(10) & 0xFF
    if k == ord('x'):
        break
    if k == ord('s'):
        puntos = []
video.release()
cv2.destroyAllWindows()