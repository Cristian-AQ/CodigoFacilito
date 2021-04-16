import cv2

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)

while True:
    ret,frame = video.read()
    if ret == True:
        frame = cv2.flip(frame,1)
        face = faceClassif.detectMultiScale(frame,1.1,5)
        for (x,y,w,h) in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('VIDEO',frame)
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

video.release()
cv2.destroyAllWindows()