import cv2
import numpy as np

video = cv2.VideoCapture('caras\isabel.mp4')

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
#creamos un kernel para mejorar la img binaria
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3)) 
while True:
    ret,frame = video.read()
    if ret == False: break
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #colocamos un mensaje en el frame
    cv2.rectangle(frame, (0,0), (frame.shape[1],40), (0,0,0),-1)
    color = (0,255,0)
    mensaje = 'No se detecto movimiento'
    #seleccionamos el area donde se detectara el movimiento
    area_pts = np.array([[230,150],[300,150],[340,frame.shape[0]],[230,frame.shape[0]]])
    
    #para realizar la deteccion en un area determinada nos apoyamos en una imgAux
    imgAux = np.zeros(shape=(frame.shape[:2]),dtype=np.uint8)
    #ponemos el area seleccionada en blanco
    imgAux = cv2.drawContours(imgAux,[area_pts],-1,255,-1)
    img_area = cv2.bitwise_and(gris, gris, mask=imgAux)
    
    #aplicamos la sustraccion de fondo
    fgmask = fgbg.apply(img_area)
    #para la reduccion de ruido en la img
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.dilate(fgmask, None, iterations=2)
    
    #encontramos los contornos en fgmask
    cnt = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for c in cnt:
        if cv2.contourArea(c)>10:
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)
            mensaje = 'Se detecto movimiento'
            color = (0,0,255)

    cv2.drawContours(frame,[area_pts],-1,color,2)
    cv2.putText(frame, mensaje, (10,30), 5, 1, color,2)

    cv2.imshow('A', fgmask)
    cv2.imshow('B', frame)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
video.release()
cv2.destroyAllWindows()