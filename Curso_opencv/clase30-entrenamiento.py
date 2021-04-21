import cv2
import os
import numpy as np
#esta parte nos muestra todos los archivos dentro de dataPath
#dataPath = 'C:/Users/51927/Desktop/caras/caras_video'
dataPath = 'caras/caras_video'
peopleList = os.listdir(dataPath)
print(peopleList)

#creamos esta parte para asignar etiquetas a cada carpeta q hubiera para asi reconocer a kien pertenece las imagenes
labels = []
faceData = []
label = 0

#especificamos la ruta de las carpetas
for nameDir in peopleList:
    personPath = dataPath+'/'+nameDir
    print('Leyendo las imagenes')

    #leemos las imagenes de cada carpeta
    for fileName in os.listdir(personPath):
        #agregamos identificador para cada imagen
        labels.append(label)
        #agregamos img en escala de grises
        faceData.append(cv2.imread(personPath+'/'+fileName,0))
        img = cv2.imread(personPath+'/'+fileName,0)
        
    label = label + 1
#modelos
face_recognizer = cv2.face.EigenFaceRecognizer_create()
face_recognizer = cv2.face.FisherFaceRecognizer_create()
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

print('entrenando...')
face_recognizer.train(faceData,np.array(labels))

#almacenamiento del entrenamiento puede ser en xml o yaml
#especificar la ruta, sino se creara donde se encuentra el script
face_recognizer.write('caras/modelos/modeloFace.xml')
print('modelo almacenado...')

