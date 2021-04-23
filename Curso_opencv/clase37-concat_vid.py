import cv2
import imutils

video = cv2.VideoCapture(0)
while True:
    ret,frame = video.read()
    frame = cv2.flip(frame, 1)
    #video tiene por default 480-v 640-h 
    if ret == False: break
    videoGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _,th = cv2.threshold(videoGray, 100, 255, cv2.THRESH_BINARY)
    #no se puede concatenar img, video que tengan diferente canal
    #por eso se convierte videoGray y th para q tengan 3 canales debido a la cam
    videoGray = cv2.cvtColor(videoGray, cv2.COLOR_GRAY2BGR)
    th = cv2.cvtColor(th, cv2.COLOR_GRAY2BGR)

    #concatenando los videos

    #videoGray = imutils.resize(videoGray,height=int(videoGray.shape[0]/2))
    #th = imutils.resize(th,height=int(th.shape[0]/2))

    videoGray = imutils.resize(videoGray,height=240)
    th = imutils.resize(th,height=240)

    videoV = cv2.vconcat([videoGray,th])
    videoH = cv2.hconcat([frame,videoV])

    #titulos
    cv2.putText(videoH, 'Streaming', (10,25), 5, 1.5, (0,255,0),2,cv2.LINE_AA)
    cv2.putText(videoH, 'Gray', (650,25), 5, 1.5, (0,255,0),2,cv2.LINE_AA)
    cv2.putText(videoH, 'Threshold', (650,265), 5, 1.5, (0,255,0),2,cv2.LINE_AA)

    cv2.imshow('A', videoH)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('x'):
        break
video.release()
cv2.destroyAllWindows()