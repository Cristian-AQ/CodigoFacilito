from flask import Flask
from flask import render_template
from flask import Response
from camara import videoCamara
from flask import request
import os
import cv2
import numpy as np

app = Flask(__name__)

def gen(camara):
    while True:
        frame = camara.get_frame()
        yield(b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" +
                frame + b"\r\n")
        
def capture(camara,name,path):
    while True:
        frame = camara.frame_capture(name,path)
        yield(b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" +
                frame + b"\r\n")
        
def dir(name):
    raiz = 'web_face_flask/Rostros Encontrados/'
    personaPath = raiz+name
    os.mkdir(personaPath)
    return personaPath

def train():
    raiz = 'web_face_flask/Rostros Encontrados/'
    peopleList = os.listdir(raiz)
    labels = []
    faceData = []
    label = 0
    for nameDir in peopleList:
        personPath = raiz+'/'+nameDir
        print('Leyendo las imagenes')

        for fileName in os.listdir(personPath):
            labels.append(label)
            faceData.append(cv2.imread(personPath+'/'+fileName,0))
        
        label = label + 1
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()

    print('entrenando...')
    face_recognizer.train(faceData,np.array(labels))
    
    face_recognizer.write('web_face_flask/modelo/modeloFace.xml')
    print('modelo almacenado...')

def detected(camara):
    while True:
        frame = camara.detected_face()
        yield(b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" +
                frame + b"\r\n")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/videoFace")
def videoFace():
    return Response(gen(videoCamara()),mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route('/storage',methods=['POST'])
def store():
    _name = request.form['name']
    print(_name)
    path = dir(_name)
    return Response(capture(videoCamara(),_name,path),mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route('/train')
def new_train():
    train()
    t = {'code':200}
    return t

@app.route("/detectedFace")
def detectedFace():
    return Response(detected(videoCamara()),mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    app.run(debug=True)