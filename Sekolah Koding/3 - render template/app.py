from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# blog

@app.route('/blog/')
def blog():
    context = {
        'judul':'blog awal',
        'author':'Anshar'
    }
    return render_template('blog/index.html', blog1 = context)

@app.route('/blog/<int:inputo>')
def blogto(inputo):
    context = {
        'judul':'blog statis',
        'author':f'Anshar {inputo}'
    }
    return render_template('blog/index.html', nomorblog = inputo, blog1 = context)