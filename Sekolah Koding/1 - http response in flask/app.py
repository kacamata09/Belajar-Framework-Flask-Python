from flask import Flask

aplikasi = Flask(__name__)

@aplikasi.route('/')
def hello():
    return '<h1>Hello Worldo!</h1>'

@aplikasi.route('/blog')
def blog():
    return '<h1>Hello Worldo! watashi wa blogto</h1>'

