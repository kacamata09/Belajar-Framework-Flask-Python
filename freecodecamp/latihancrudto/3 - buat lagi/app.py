from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# koneksi database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/testflask'
dbku = SQLAlchemy(app)

# class model flask untuk buat tabel
class Mahasiswa(dbku.Model):
    nimstring = dbku.Column(dbku.String(20), primary_key = True)
    namamahasiswa = dbku.Column(dbku.String(100), nullable = False)
    alamat = dbku.Column(dbku.String(100), nullable=True)
    tanggal_masuk = dbku.Column(dbku.DateTime, default=datetime.utcnow)
    
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nim = request.form['nimmaha']
        nama = request.form['namamaha']
        alamat = request.form['alamatmaha']
        mahasiswa_baru = Mahasiswa(nimstring=nim, namamahasiswa=nama, alamat=alamat)
        # mahasiswa_baru = Mahasiswa(nimstring=nim)
        mahasiswa_baru1 = Mahasiswa(namamahasiswa=nama)
        mahasiswa_baru2= Mahasiswa(alamat=alamat)
        dbku.session.add(mahasiswa_baru)
        # dbku.session.add(mahasiswa_baru1)
        # dbku.session.add(mahasiswa_baru2)
        dbku.session.commit()
        return redirect('/')
    
    tampilkan = Mahasiswa.query.order_by(Mahasiswa.tanggal_masuk).all()
    return render_template('index.html', konten = tampilkan)


@app.route('/hapus/<nimma>')
def hapus(nimma):
    # nimmahasiswa = Mahasiswa.query.get_or_404(nimma)
    nimmahasiswa = Mahasiswa.query.get(nimma)
    dbku.session.delete(nimmahasiswa)
    dbku.session.commit()
    return redirect('/')

@app.route('/edit/<nimma>', methods=['GET', 'POST'])
def edit(nimma):
    nimmahasiswa = Mahasiswa.query.get(nimma)
    if request.method == 'POST':
        nimmahasiswa.nimstring = request.form['nimmaha']
        nimmahasiswa.namamahasiswa = request.form['namamaha']
        nimmahasiswa.alamat = request.form['alamatmaha']
        dbku.session.commit()
        return redirect('/')
    
    return render_template('edit.html', konten = nimmahasiswa)
        
        
    
if __name__ == '__main__':
    app.run(debug=True)
    