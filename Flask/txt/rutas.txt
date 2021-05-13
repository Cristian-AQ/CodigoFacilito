from flask import Flask
from flask import request#permite trabajar con parametros

app = Flask(__name__)

@app.route('/')
def index():
	return 'hola mundo'

@app.route('/saluda')
def saluda():
	return 'otro mensaje'

#http://localhost:8000/params?params1=Cristian
#http://localhost:8000/params

@app.route('/params')
def params():
	param = request.args.get('params1','no contiene el parametro')
	return 'El parametro es : {}'.format(param)

if __name__ == '__main__':
	app.run(debug = True, port = 8000)