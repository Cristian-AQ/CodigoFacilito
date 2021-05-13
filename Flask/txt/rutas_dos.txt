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
@app.route('/params/<name>/<last_name>/<int:edad>')
def params(name='valor por default', last_name='nada',edad='nada'):
	return 'El parametro es : {} {} {}'.format(name, last_name, edad)

if __name__ == '__main__':
	app.run(debug = True, port = 8000)