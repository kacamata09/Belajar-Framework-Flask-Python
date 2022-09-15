from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''<h1>ini indexto</h1> 
<a href="/blog">Ini blogto</a> ''' 

@app.route('/blog')
def blog():
    return '''<h1>ini indexto</h1> 
<a href="/">Ini hometo</a> ''' 

@app.route('/blog/<inputo>')
def blogstatis(inputo):
    cobadecimalto = 1000
    return '<h1>ini url statis : %s %d</h1>' % (inputo, cobadecimalto)

@app.route('/blog/integer/<int:integer>')
def bloginteger(integer):
    cobadecimalto = 1000
    return '<h1>ini url statis integer : %d %d</h1>' % (integer, cobadecimalto)
