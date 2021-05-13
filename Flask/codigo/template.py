from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('web.html')#necesario crear la carpeta de nombre template

if __name__ == '__main__':
	app.run(debug = True, port = 8000)