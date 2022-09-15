from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

dbku = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='crudlatihanflask'
)

app = Flask(__name__)

# @app.route('/', methods = ['GET', 'POST'])
# def index():
    
#     return render_template('index.html')

@app.route('/', methods = ['GET', 'POST'])
def fungsisimpan():
    if request.method == 'POST':
        nama = request.form['namamahasiswa']
        nim = int(request.form['nimmahasiswa'])
        alamat = request.form['alamatyou']
        mahasiswa = nama, nim, alamat
        sqlnyabro = 'insert into mahasiswa values(%s, %s, %s)'
        cursorbro = dbku.cursor()
        cursorbro.execute(sqlnyabro, mahasiswa)
        dbku.commit()
        return redirect(url_for('tampilmahasiswa'))
        
    return render_template('index.html')

@app.route('/mahasiswa')
def tampilmahasiswa():
    return render_template('mahasiswa.html')