from flask import Flask, render_template

aplikasi = Flask(__name__)

@aplikasi.route('/<inputo>')
def index(inputo):
    context =  {
        'nama':'Anshar',
        'judul':'Home'
    }
    return render_template('index.html', usern=context)