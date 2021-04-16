import cv2 
import numpy as np

video = cv2.VideoCapture(0)

bg = None

azulBajo = np.array([100,100,20],np.uint8)
azulAlto = np.array([125,255,255],np.uint8)

while True:
    ret,frame = video.read()
    if ret == True:
        if bg is None:#almacenamos la captura
            bg = cv2.flip(frame,1)
        frame = cv2.flip(frame,1)
        frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        maskAzul = cv2.inRange(frameHSV,azulBajo,azulAlto)
        maskAzul = cv2.medianBlur(maskAzul,11)#filtro para suavizar imagen
        kernel = np.ones((10,10),np.uint8)
        maskAzul = cv2.dilate(maskAzul,kernel)#para eliminar bordes (incrementa la region blanca)
        
        area_color = cv2.bitwise_and(bg,bg,mask=maskAzul)
        inv_mask = cv2.bitwise_not(maskAzul)
        area_sin_color = cv2.bitwise_and(frame,frame,mask=inv_mask)
        invisible = cv2.addWeighted(area_color,1,area_sin_color,1,0)
        cv2.imshow('INVISIBLE',invisible)
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

video.release()
cv2.destroyAllWindows()