import cv2
import os#ayuda a listar archivos, crearlos, ect

imagenesPath = 'C:/Users/51927/Desktop/caras'#guardamos la ruta del folder; despues de : va /
imagenesPathList = os.listdir(imagenesPath)#listamos el contenido de la ruta
print(imagenesPathList)

#creamos una carpeta para almacenar los rostros encontrados

if not os.path.exists('Rostros Encontrados'):
    print('Carpeta creada: Rostros Encontrados')
    os.mkdir('C:/Users/51927/Desktop/Rostros Encontrados')#especificar ruta y nombre de la carpeta, por defecto se crea en la ubicacion del Script

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

cont = 0

for imagen in imagenesPathList:
    img = cv2.imread(imagenesPath+'/'+imagen)
    img = cv2.resize(img,(600,400))
    imgAux = img.copy()
    gris = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    face = faceClassif.detectMultiScale(gris,1.11,5)

    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.rectangle(img,(10,5),(450,25),(255,255,255),-1)
    mensaje1 = 'Presione \'s\' para guardar los rostros encontrados'
    cv2.putText(img,mensaje1,(10,20),2,0.5,(128,0,255),1,cv2.LINE_AA)

    cv2.rectangle(img,(10,365),(230,385),(255,255,255),-1)
    mensaje2 = 'Presione \'x\' para salir'
    cv2.putText(img,mensaje2,(10,380),2,0.5,(128,0,255),1,cv2.LINE_AA)
    
    cv2.imshow('IMAGEN',img)
    k = cv2.waitKey(0)
    if k == ord('s'):
        for (x,y,w,h) in face:
            rostro = imgAux[y:y+h,x:x+w]#cortando la imagen
            rostro = cv2.resize(rostro,(60,60))
            #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.imwrite(f'C:/Users/51927/Desktop/Rostros Encontrados/captura{cont}.jpg',rostro)
            cont = cont + 1
            cv2.imshow('ROSTRO',rostro)
            cv2.waitKey(0)
    if k == ord('x'):
        break
cv2.destroyAllWindows()
