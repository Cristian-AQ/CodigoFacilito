from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/web/<name>')
def web(name = 'Giratina', age ='none'):
	age = 17
	my_list = [1,2,3,4]
	return render_template('web.html', name=name, age=age, list=my_list)#necesario crear la carpeta de nombre template

if __name__ == '__main__':
	app.run(debug = True, port = 8000)