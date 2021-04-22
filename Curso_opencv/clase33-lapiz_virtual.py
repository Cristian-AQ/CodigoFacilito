import cv2
import numpy as np

video = cv2.VideoCapture(0)

azulBajo = np.array([100,100,20],np.uint8)
azulAlto = np.array([125,255,255],np.uint8)

#caja colores
colorCele = (255,113,82)
colorAmarillo = (89,222,255)
colorRosa = (128,0,255)
colorVerde = (0,255,36)
colorLimpPantalla = (29,112,246)#limpia pantalla

#grosor de lineas de la caja de colores cuando se selecciona
grosorCele = 6
grosorAmarillo = 2
grosorVerde = 2
grosorRosa = 2

#grosor del marcado para dibujar
grosorPeq = 6
grosorMed = 2
grosorGran = 2

#lapiz virtual
color = colorCele#color entrada
grosor = 3#grosor del marcador

x1 = None
y1 = None
imAux = None

while True:
    ret,frame = video.read()
    if ret == False: break
    frame = cv2.flip(frame, 1)
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    if imAux is None:
        #creamos un frame con tamaño por defecto
        #lo utilizaremos como lienzo para dibujar
        imAux = np.zeros(frame.shape,dtype=np.uint8)
    #ubicando los cuadros de los colores
    cv2.rectangle(frame,(0,0),(50,50),colorAmarillo,grosorAmarillo)
    cv2.rectangle(frame, (50,0), (100,50), colorRosa,grosorRosa)
    cv2.rectangle(frame, (100,0), (150,50), colorVerde,grosorVerde)
    cv2.rectangle(frame, (150,0), (200,50), colorCele,grosorCele)

    #ubicando cuadro de limpiar pantalla
    cv2.rectangle(frame, (300,0), (400,50), colorLimpPantalla,1)
    cv2.putText(frame, 'Limpiar', (320,20), 6, 0.6, colorLimpPantalla,1,cv2.LINE_AA)
    cv2.putText(frame, 'Pantalla', (320,40), 6, 0.6, colorLimpPantalla,1,cv2.LINE_AA)

    #ubicando cuadro de grosor de linea
    cv2.rectangle(frame, (490,0), (540,50), (0,0,0),grosorPeq)
    cv2.circle(frame, (515,25), 3, (0,0,0),-1)
    cv2.rectangle(frame, (540,0), (590,50), (0,0,0),grosorMed)
    cv2.circle(frame, (565,25), 7, (0,0,0),-1)
    cv2.rectangle(frame, (590,0), (640,50), (0,0,0),grosorGran)
    cv2.circle(frame, (615,25), 11, (0,0,0),-1)
    
    maskAzul = cv2.inRange(frameHSV, azulBajo, azulAlto)
    maskAzul = cv2.erode(maskAzul,None,iterations=1)
    maskAzul = cv2.dilate(maskAzul,None,iterations=2)
    maskAzul = cv2.medianBlur(maskAzul, 11)

    #buscando contornos

    cnt,_ = cv2.findContours(maskAzul, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #tomamos el contorno mas grande
    cnt = sorted(cnt,key=cv2.contourArea,reverse=True)[:1]
    for c in cnt:
        area = cv2.contourArea(c)
        if area >1000:
            x,y2,w,h = cv2.boundingRect(c)
            #cv2.rectangle(frame, (x,y2), (x+w,y2+h), (0,255,0),2)
            #tiene que ser entero necesariamente
            x2 = int(x + w/2)
            if x1 is not None:
                #colores
                if 0 < x2 <50 and 0 < y2 <50:
                    color = colorAmarillo
                    grosorAmarillo = 6
                    grosorRosa = 2
                    grosorVerde = 2
                    grosorCele = 2
                if 50 < x2 <100 and 0 < y2 <50:
                    color = colorRosa
                    grosorAmarillo = 2
                    grosorRosa = 6
                    grosorVerde = 2
                    grosorCele = 2
                if 100 < x2 <150 and 0 < y2 <50:
                    color = colorVerde
                    grosorAmarillo = 2
                    grosorRosa = 2
                    grosorVerde = 6
                    grosorCele = 2
                if 150 < x2 <200 and 0 < y2 <50:
                    color = colorCele
                    grosorAmarillo = 2
                    grosorRosa = 2
                    grosorVerde = 2
                    grosorCele = 6
                #grosor  de linea
                if 490 < x2 <540 and 0 < y2 <50:
                    grosor = 3
                    grosorPeq = 6
                    grosorMed = 1
                    grosorGran = 1
                if 540 < x2 <590 and 0 < y2 <50:
                    grosor = 7
                    grosorPeq = 1
                    grosorMed = 6
                    grosorGran = 1
                if 590 < x2 <640 and 0 < y2 <50:
                    grosor = 11
                    grosorPeq = 1
                    grosorMed = 1
                    grosorGran = 6
                #limpiar pantalla
                if 300 < x2 < 400 and 0 < y2 < 50:
                    cv2.rectangle(frame, (300,0), (400,50), colorLimpPantalla,1)
                    cv2.putText(frame, 'Limpiar', (320,20), 6, 0.6, colorLimpPantalla,2,cv2.LINE_AA)
                    cv2.putText(frame, 'Pantalla', (320,40), 6, 0.6, colorLimpPantalla,2,cv2.LINE_AA)
                    imAux = np.zeros(frame.shape,dtype=np.uint8)
                #para que no pinte la parte superior
                if 0 < y2 < 60 or 0 < y1 < 60:
                    imAux = imAux
                #dibujo de trazos
                else:
                   imAux = cv2.line(imAux, (x1,y1), (x2,y2), color,grosor)
            #obtener los valores de x1, y1, seran actualizados con los valores de x2, y2
            #para asi obtener un valor actual y otro pasado
            cv2.circle(frame, (x2,y2), grosor, color,3)
            x1 = x2
            y1 = y2                            
        else:
            x1 = None
            y1 = None
    #hacer que se vea en el frame
    imAuxGray = cv2.cvtColor(imAux, cv2.COLOR_BGR2GRAY)
    _,th = cv2.threshold(imAuxGray, 10, 255, cv2.THRESH_BINARY)
    thInv = cv2.bitwise_not(th)
    frame = cv2.bitwise_and(frame, frame, mask=thInv)
    frame = cv2.add(frame,imAux)

    cv2.imshow('A', frame)
    cv2.imshow('B',imAux)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
video.release()
cv2.destroyAllWindows()