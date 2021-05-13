from flask import Flask
from flask import request#permite trabajar con parametros

app = Flask(__name__)

@app.route('/')
def index():
	return 'hola mundo'

@app.route('/saluda')
def saluda():
	return 'otro mensaje'

#http://localhost:8000/params?params1=Cristian ahi estamos llenado el parametro
#http://localhost:8000/params

@app.route('/params')
def params():
	param = request.args.get('params1','no contiene el parametro')#la segunda cadena es el default
	return f'El parametro es : {param}'

if __name__ == '__main__':
	app.run(debug = True, port = 8000)