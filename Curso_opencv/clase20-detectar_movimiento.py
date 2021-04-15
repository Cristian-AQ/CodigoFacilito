import cv2
import numpy as np

video = cv2.VideoCapture(0)

i = 0
while True:
    ret,frame = video.read()
    if ret == True:
        frame = cv2.flip(frame,1)
        gris = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        if i == 20:
            bgGray = gris#captura el frame 20 y lo almacena
        if i > 20:
            dif = cv2.absdiff(gris,bgGray)
            _,th = cv2.threshold(dif,40,255,cv2.THRESH_BINARY)
            cnt,_ = cv2.findContours(th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            cv2.imshow('B',th)
            for c in cnt:
                area = cv2.contourArea(c)#devolver el area en px de cada contorno
                if area > 9000:#area mayor se encierra en rectangulo
                    x,y,w,h = cv2.boundingRect(c)#devuelve 4 valores
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('VIDEO',frame)
        i=i+1
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break
video.release()
cv2.destroyAllWindows()