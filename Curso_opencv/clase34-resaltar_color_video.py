import cv2
import numpy as np
import imutils

azulBajo = np.array([95,100,20],np.uint8)
azulAlto = np.array([135,255,255],np.uint8)

video = cv2.VideoCapture(0)
while True:
    ret,frame = video.read()
    if ret == False: break
    frame = cv2.flip(frame, 1)
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameGray = cv2.cvtColor(frameGray, cv2.COLOR_GRAY2BGR)
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    maskAzul = cv2.inRange(frameHSV, azulBajo, azulAlto)
    azulDetec = cv2.bitwise_and(frame, frame,mask=maskAzul)

    invMask = cv2.bitwise_not(maskAzul)
    bgGray = cv2.bitwise_and(frameGray,frameGray,mask=invMask)

    frameFinal = cv2.add(bgGray,azulDetec)
   
    cv2.imshow('A', frameFinal)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

video.release()
cv2.destroyAllWindows()