import cv2

imagen = cv2.imread('img\poligonos.png')
gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gris,10,150)

cnt,_ = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for c in cnt:
    epsilon = 0.008*cv2.arcLength(c,True)
    aprox = cv2.approxPolyDP(c,epsilon,True)

    x,y,w,h, = cv2.boundingRect(aprox)

    if len(aprox) == 3:
        cv2.putText(imagen,'TRIANGULO',(x,y-10),1,1,0,2)
    if len(aprox) == 4:
        aspec_radio = float(w)/h
        if aspec_radio == 1:
            cv2.putText(imagen,'CUADRADO',(x,y-10),1,1,0,2)
        else:
            cv2.putText(imagen,'RECTANGULO',(x,y-10),1,1,0,2)
    if len(aprox) == 5:
        cv2.putText(imagen,'PENTAGONO',(x,y-10),1,1,0,2)
    if len(aprox) == 6:
        cv2.putText(imagen,'HEXAGONO',(x,y-10),1,1,0,2)
    if len(aprox) > 10:
        cv2.putText(imagen,'CIRCULO',(x,y-10),1,1,0,2)

    cv2.drawContours(imagen,[aprox],0,(0,255,0),2)
    cv2.imshow('POLIGONOS',imagen)
    cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()