import cv2
import numpy as np
import imutils

video = cv2.VideoCapture('caras/carros.mp4')

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
#contador de autos
car_counter = 0

while True:
    ret,frame = video.read()
    if ret == False: break
    #frame = imutils.resize(frame,width=640)
    #creamos nuestra area de interes
    area_pts = np.array([[330,216],[frame.shape[1]-80,216],[frame.shape[1]-80,271],[330,271]])
    

    imAux = np.zeros(shape=(frame.shape[:2]),dtype=np.uint8)
    #pintamos nuestra area de interes de blanco
    imAux = cv2.drawContours(imAux, [area_pts], -1, (255),-1)
    #mostrar el frame en imAux 
    img_area = cv2.bitwise_and(frame, frame,mask=imAux)

    #aplicamos la sustraccion de fondo
    fgmask = fgbg.apply(img_area)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
    #sirve para conectar las areas blancas mas grandes
    fgmask = cv2.dilate(fgmask, None, iterations=5)

    cnt = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    for c in cnt:
        if cv2.contourArea(c) > 1500:
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,255),1)
            #contando los autos
            if 440 < (x+w)<460:
                car_counter = car_counter + 1
                cv2.line(frame, (450,216), (450,271), (0,255,0),3)

    
    cv2.drawContours(frame, [area_pts], -1, (0,255,0),2)
    #dibujando linea amarilla
    cv2.line(frame, (450,216), (450,271), (0,255,255),1)
    #dibujando un rectangulo para el contador
    cv2.rectangle(frame, (frame.shape[1]-70,215), (frame.shape[1]-5,270), (0,255,0),2)
    cv2.putText(frame, str(car_counter), (frame.shape[1]-55,250), 0, 1.2, (0,255,0),2)
    cv2.imshow('A', frame)
    #cv2.imshow('B', fgmask)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
video.release()
cv2.destroyAllWindows()