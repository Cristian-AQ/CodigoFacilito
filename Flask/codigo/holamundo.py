from flask import Flask

app = Flask(__name__)#nuevo objeto

@app.route('/')#wrap o un decorador
def index():#funcion
 return 'hola mundo'#regresar un string

app.run()#se encarga de ejecutar el servidor 5000