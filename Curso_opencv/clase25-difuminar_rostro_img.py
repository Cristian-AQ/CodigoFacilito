import cv2

def onChange(value):
    pass

imagen = cv2.imread('img\oficina.png')
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
cv2.namedWindow('A')
cv2.createTrackbar('value','A',0,10,onChange)

while True:
    val = cv2.getTrackbarPos('value','A')
    face = faceClassif.detectMultiScale(imagen,1.1,5)

    for (x,y,w,h) in face:
        if val > 0:
            imagen[y:y+h,x:x+w] = cv2.blur(imagen[y:y+h,x:x+w],(val,val))
        else:
           imageN = imagen.copy()
        
    cv2.imshow('A',imagen)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()