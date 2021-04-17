import cv2
import numpy as np

imagen = 255*np.ones((400,600,3),dtype=np.uint8)#imagen blanco

#linea
cv2.line(imagen,(0,0),(600,400),(0,255,0),3)
#rectangulo p1(esquina_superior_izquierdo) p2(esquina_inferior_derecha)
cv2.rectangle(imagen,(10,10),(400,300),(0,255,0),3)
#circulo
cv2.circle(imagen,(300,200),100,(0,255,0),3)#valor de -1 llena el circulo
#texto
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagen,'GAA',(10,30),font,1,(255,0,255),1,cv2.LINE_AA)#el 3 argumento es la ubicacion

cv2.imshow('IMAGEN',imagen)
k = cv2.waitKey(0)
cv2.destroyAllWindows()