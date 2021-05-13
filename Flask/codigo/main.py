from flask import Flask
from flask import render_template

import form

app = Flask(__name__)

@app.route('/')
def index():
	comment_form = form.CommentForm()
	title = "Curso Flask"
	return render_template('index.html', title = title, form = comment_form)
if __name__ == '__main__':
	app.run(debug=True, port=8000)