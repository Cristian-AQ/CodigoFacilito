import cv2
import numpy as np

video = cv2.VideoCapture(0)

azulBajo = np.array([100,100,20],np.uint8)
azulAlto = np.array([125,255,255],np.uint8)

while True:
    ret,frame = video.read()
    if ret == True:
        frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HLS)
        mask = cv2.inRange(frameHSV,azulBajo,azulAlto)
        #obtener contorno
        contorno,hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        #dibujar contorno en la imagen
        #cv2.drawContours(frame,contorno,-1,(255,0,0),3)#-1 = dibuja todos los contornos,3=grosor de contorno
        for c in contorno:
            area = cv2.contourArea(c)
            if area > 3000:
                M = cv2.moments(c)#ubicar el centro
                if (M['m00']==0):
                    M['m00']=1
                x = int(M['m10']/M['m00'])
                y = int(M['m01']/M['m00'])
                #el centro es un circulo, sin esto no se sabria donde esta el centro
                #puede usarse cualquier figura para el centro
                #cv2.circle(frame,(x,y),7,(0,255,0),1)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame,f'{x},{y}',(x+10,y),font,0.75,(0,255,0),1,cv2.LINE_AA)
                #suavizado de contorno
                nuevoContorno = cv2.convexHull(c)
                cv2.drawContours(frame,[nuevoContorno],0,(255,0,0),3)#[se coloca los contornos seleccionados]
        cv2.imshow('M',mask)
        cv2.imshow('V',frame)
        if cv2.waitKey(1)  & 0xFF == ord('x'):
            break
video.release()
cv2.destroyAllWindows()
