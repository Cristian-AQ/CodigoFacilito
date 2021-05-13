from flask import Flask
from flask import request#permite trabajar con parametros

app = Flask(__name__)

@app.route('/')
def index():
	return 'hola mundo'

@app.route('/saluda')
def saluda():
	return 'otro mensaje'
@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<last_name>')
@app.route('/params/<name>/<last_name>/<float:edad>')#int permite recibir solamente numeros enteros
def params(name='valor por default', last_name='nada',edad='nada'):
	return f'El parametro es : {name} {last_name} {edad}'

if __name__ == '__main__':
	app.run(debug = True, port = 8000)