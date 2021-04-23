import cv2
import imutils

img1 = cv2.imread('caras/emotion/diablito.jpg')
img2 = cv2.imread('caras/emotion/sonrisa.jpg')
img3 = cv2.imread('caras/emotion/molesta.jpg')

#saber las dimensiones y canales de las imagenes se utiliza img.shape
#solo se puede concatenar img que tenga v y h igual

#unir imagenes horizontal
horizontal1 = cv2.hconcat([img1,img2,img3])
#unir imagenes vertical
vertical = cv2.vconcat([img1,img2,img3])

#jugando
horizontal1 = cv2.hconcat([img1,img2,img3])
horizontal2 = cv2.hconcat([img3,img2,img1])
vertical1 = cv2.vconcat([horizontal1,horizontal2])

cv2.imshow('A', vertical1)
cv2.waitKey(0)
cv2.destroyAllWindows()
