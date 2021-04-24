import cv2
import imutils

video = cv2.VideoCapture('caras/isabel.mp4')
#la img cuanta con 4 canales, utilizaremos la transparencia con unchanged
img = cv2.imread('caras/emotion/MOLESTA.png',cv2.IMREAD_UNCHANGED)
#cv2.imshow('A', img[:,:,3])#para ver la transparencia(negro)
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

while True:
    ret,frame = video.read()
    #frame = cv2.flip(frame, 1)
    if ret == False: break
    face = faceClassif.detectMultiScale(frame,1.3,5)

    for (x,y,w,h) in face:
        #cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)
        #redimensionando img para que se adapte al rostro
        resized_img = imutils.resize(img,width=w,height=h)
        filas_img = resized_img.shape[0]
        col_img = w
        '''
        #ubicamos la img de acorde al rostro
        porcion_alto = filas_img//4#es un entero

        #se produce un error cuando la img sale del frame por ello se pone
        if y - filas_img >=0:
            #tomamos una porcion del video y ponemos la img redimensionada
            n_frame = frame[y-filas_img+porcion_alto:y+porcion_alto,x:x+w]
            
            #fotogramas de la img redimensionada
            mask = resized_img[:,:,3]
            mask_inv = cv2.bitwise_not(mask)
            #hacemos q se muestre a color y negro el fondo
            bg_black = cv2.bitwise_and(resized_img, resized_img,mask=mask)
            #resized_img tiene 4 canales, entonces tomamos solo 3 
            bg_black = bg_black[:,:,0:3]
            #hacemos que la silueta del gorro este en negro
            bg_frame = cv2.bitwise_and(n_frame, n_frame, mask=mask_inv)
            #juntamos ambas img
            result = cv2.add(bg_black, bg_frame)
            #colocamos la img en el frame principal
            frame[y-filas_img+porcion_alto:y+porcion_alto,x:x+w] = result
        ''' 
        #kitamos la incomodidad de adecuar el rostro
        dif =0
        porcion_alto = filas_img

        if y - filas_img + porcion_alto>=0:
            n_frame = frame[y-filas_img+porcion_alto:y+porcion_alto,x:x+w]
        else:
            dif = abs(y-filas_img+porcion_alto)
            n_frame = frame[0:y+porcion_alto,x:x+w]
        
        mask = resized_img[:,:,3]
        mask_inv = cv2.bitwise_not(mask)
            
        bg_black = cv2.bitwise_and(resized_img, resized_img,mask=mask)     
        bg_black = bg_black[dif:,:,0:3]
        bg_frame = cv2.bitwise_and(n_frame, n_frame, mask=mask_inv[dif:,:])    
        
        result = cv2.add(bg_black, bg_frame)
        if y - filas_img + porcion_alto>=0:
            frame[y-filas_img+porcion_alto:y+porcion_alto,x:x+w] = result
        else:
            frame[0:y+porcion_alto,x:x+w] = result
            
    cv2.imshow('A', frame)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

video.release()
cv2.destroyAllWindows()