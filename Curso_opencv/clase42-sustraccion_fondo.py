import cv2

video = cv2.VideoCapture(0)

#con esto detectamos objetos en movimiento, si no se mueven se podria decir que "desaparecen"
#se crea un fondo por defecto
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

#similar al anterior solo que se adapta mejor a los cambios de iluminacion
fgbg = cv2.createBackgroundSubtractorMOG2()

#esta realiza 120 capturas al comienzo del video (por eso se ve negro al comienzo) y luego detecta los movimientos
#para mejorar se deben utilizar tecnicas de suavizado
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

while True:
    ret,frame = video.read()
    frame = cv2.flip(frame, 1)
    if ret == False: break
    #nos permite obtener la mascara de primer plano, es decir obtendremos una img binaria
    #esta line se utiliza para todo
    fgmask = fgbg.apply(frame)
    cv2.imshow('A', fgmask)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
video.release()
cv2.destroyAllWindows()