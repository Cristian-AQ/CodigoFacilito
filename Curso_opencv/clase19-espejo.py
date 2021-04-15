import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:
    ret,frame = video.read()
    if ret == True:
        #flip = cv2.flip(frame,1)#espejo
        ancho = frame.shape[1]//2
        frame[:,:ancho] = cv2.flip(frame[:,ancho:],1)
        cv2.imshow('ESPEJO',frame)
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

video.release()
cv2.destroyAllWindows()