import cv2

video = cv2.VideoCapture('video\VideoPrueba.avi')

while (video.isOpened()):#lee la imagen a cada momento
    ret,imagen = video.read()
    if ret == True:
        cv2.imshow('Video',imagen)
        if cv2.waitKey(500) & 0xFF == ord('x'):#0xff si se trabaja en maquina de 65 bits
            break                           #ord tecla que detiene el proceso
        else:#para que cierre la ventana del video
            break
video.release()#cerrar la captura
cv2.destroyAllWindows()