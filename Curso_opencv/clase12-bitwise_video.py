import cv2
import numpy as np

video = cv2.VideoCapture(0)
mask = np.zeros((480,640),dtype=np.uint8)
mask = cv2.circle(mask,(320,240),125,(255),-1)
mask = cv2.bitwise_not(mask)#si lo quitas solo mustra en un circulo el video

while True:
    ret,frame = video.read()
    if ret == True:
        maskP = cv2.bitwise_and(frame,frame,mask=mask)
        cv2.imshow('V',maskP)
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break
video.release()
cv2.destroyAllWindows()

