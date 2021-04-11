import cv2
import numpy as np

bgr = cv2.imread('img\Mangekyou.png')
#bgr = np.zeros((300,300,3),dtype=np.uint8)#muestra color negro

#EN BGR
C1 = bgr[:,:,0]#muestra color en pantalla
C2 = bgr[:,:,1]
C3 = bgr[:,:,2]
cv2.imshow('BGR',np.hstack([C1,C2,C3]))
#CONVERTIR A RGB
rgb=cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB)

C1 = rgb[:,:,0]#muestra color en pantalla
C2 = rgb[:,:,1]
C3 = rgb[:,:,2]
cv2.imshow('RGB',np.hstack([C1,C2,C3]))

cv2.waitKey(0)
cv2.destroyAllWindows()