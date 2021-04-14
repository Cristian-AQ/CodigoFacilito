import cv2
import imutils

imagen1 = cv2.imread('img\maxresdefault1.jpg',0)
imagen2 = cv2.imread('img\Hiromi Maiharu.jpg',0)

imagen1 = imutils.resize(imagen1,width=400)
imagen2 = imutils.resize(imagen2,width=400)

sustraer1 = cv2.subtract(imagen1,imagen2)
sustraer2 = cv2.absdiff(imagen1,imagen2)

cv2.imshow('SUBTRACT',sustraer1)
cv2.imshow('ABSDIFF',sustraer2)

cv2.waitKey(0)
cv2.destroyAllWindows()