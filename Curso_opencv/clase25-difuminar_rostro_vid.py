import cv2

def onChange(value):
    pass
video = cv2.VideoCapture(0)
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
cv2.namedWindow('VIDEO')
cv2.createTrackbar('value','VIDEO',0,15,onChange)

while True:
    ret,frame = video.read()
    val = cv2.getTrackbarPos('value','VIDEO')
    frame = cv2.flip(frame,1)
    face = faceClassif.detectMultiScale(frame,1.1,5)
    for (x,y,w,h) in face:
        if val > 0:
            frame[y:y+h,x:x+w] = cv2.blur(frame[y:y+h,x:x+w],(val,val))
            
    cv2.imshow('VIDEO',frame)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

video.release()
cv2.destroyAllWindows()