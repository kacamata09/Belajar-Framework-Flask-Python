from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask('nama aplikasi')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/testflask'
app.config['SECRET_KEY'] = 'isi random string, apa ajalah, atau buat fungsi generator random secret key sendiri'
dbku = SQLAlchemy(app)
app.secret_key = 'adasdasdsadasfewtet'

class Anakbaru(dbku.Model):
    id_anak = dbku.Column(dbku.Integer, primary_key=True)
    nama_anak = dbku.Column(dbku.String(200), nullable=False)
    nama_ayah = dbku.Column(dbku.String(200), nullable=True)
    tanggal_bergabung = dbku.Column(dbku.DateTime, default=datetime.utcnow)
    
class Pengguna(dbku.Model):
    nama_user = dbku.Column(dbku.String(30), primary_key = True )
    kata_sandi = dbku.Column(dbku.String(30))


def validasiadakahuser():
    if 'username' in session:
        return

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html')
    else:
        return 'login dulu'
    
    # return redirect(url_for('login'))

@app.route('/pendaftaran/', methods=['GET', 'POST'])
def halaman_daftar():
    if request.method == 'POST':
        namaAnak = request.form['nama_anaktk']
        namaAyah = request.form['nama_ayahtk']
        tambah_anak = Anakbaru(nama_anak = namaAnak, nama_ayah=namaAyah)
        dbku.session.add(tambah_anak)
        dbku.session.commit()
        return redirect('/pendaftaran/')
    
    tampilkan = Anakbaru.query.order_by(Anakbaru.id_anak).all()
    return render_template('hal_pendaftaran.html', konten = tampilkan)

@app.route('/pendaftaran/hapus/<int:id_anaktk>')
def hapus(id_anaktk):
    get_id_anak = Anakbaru.query.get_or_404(id_anaktk)
    dbku.session.delete(get_id_anak)
    dbku.session.commit()
    return redirect(url_for('halaman_daftar'))
    # return redirect('/pendaftaran/')

@app.route('/pendaftaran/edit/<int:id_anaktk>', methods=['GET', 'POST'])
def edit(id_anaktk):
    get_id_anak = Anakbaru.query.get_or_404(id_anaktk)
    if request.method == 'POST':
        get_id_anak.nama_anak = request.form['nama_anaktk']
        get_id_anak.nama_ayah = request.form['nama_ayahtk']
        dbku.session.commit()
        return redirect(url_for('halaman_daftar'))

    return render_template('hal_edit.html', anak=get_id_anak)

    # return redirect('/pendaftaran/')
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        get_nama_user = request.form['username'] 
        try:
            validasiuser = Pengguna.query.get_or_404(get_nama_user)
        except:
            return 'userya gak ada woi'
         
        if validasiuser.kata_sandi == request.form['password']:
            session['username'] = get_nama_user
            return redirect(url_for('index'))
        return '<h1>salah woi passwordnya</h1>'
    
    return render_template('login.html')
    
@app.route('/logout/')
def logout():
    del session['username']
    return redirect(url_for('login'))

if __name__ == '__main__':
    # dbku.create_all()
    app.run(debug=True)