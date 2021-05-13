from flask import Flask
from flask import render_template

app = Flask(__name__)#esto asume que los html se encuentran el file templates
#app = Flask(__name__, folder_template='name_file_templates')esto asume que los html se encuentran el  file != templates

@app.route('/')
def index():
	return render_template('index.html')#necesario crear la carpeta de nombre template

if __name__ == '__main__':
	app.run(debug = True, port = 8000)