import cv2

video = cv2.VideoCapture(0)#cero xq es camara web
#grabar video
salida = cv2.VideoWriter('video\VideoPrueba.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))
#cv2.VideoWriter(nombre,codec,fotogramas,dimension)

while (video.isOpened()):#lee la imagen a cada momento
    ret,imagen = video.read()
    if ret == True:
        cv2.imshow('Video',imagen)
        salida.write(imagen)
        if cv2.waitKey(500) & 0xFF == ord('x'):#0xff si se trabaja en maquina de 65 bits
            break                           #ord tecla que detiene el proceso
video.release()#cerrar la captura
salida.release()
cv2.destroyAllWindows()