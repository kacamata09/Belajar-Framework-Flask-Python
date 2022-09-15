from flask import Flask, render_template

import mysql.connector

dbku = mysql.connector.connect()

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        'judul':'Home',
        'author':'Anshar'
    }
    return render_template('index.html', konten=context)