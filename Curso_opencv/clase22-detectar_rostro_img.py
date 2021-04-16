import cv2

#creamos el clasificador llamando al archivo xml
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

imagen = cv2.imread('img\oficina.png')
gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

#funciona tanto para color y b/n
face = faceClassif.detectMultiScale(gris,#imagen donde actua el detector
scaleFactor=1.1,#q tanto sera reducida la imagen, si es muy pequño falso positivo, muy grando omite algunas
minNeighbors=5,#cantidad de vecinos menor valor falso positivo, mayor omite algunos
minSize=(30,30),#tamaño minimo posible del objeto, rostros menores son ignorados
maxSize=(200,200))#tamano maximo posible del objeto, rostros mas grandes son ingnorados

for (x,y,w,h) in face:
    cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('A',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()