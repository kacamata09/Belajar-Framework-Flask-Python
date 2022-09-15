from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/testflask'
dbku = SQLAlchemy(app)

class Tugasbaru(dbku.Model):
    nomortugas = dbku.Column(dbku.Integer, primary_key = True)
    namatugas = dbku.Column(dbku.String(100), nullable=False)
    waktu_tugas = dbku.Column(dbku.DateTime, default=datetime.utcnow)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tugasku = request.form['initugas']
        tugas_baru = Tugasbaru(namatugas=tugasku)
        dbku.session.add(tugas_baru)
        dbku.session.commit()
        return redirect('/')
    else:
        tampilkan = Tugasbaru.query.order_by(Tugasbaru.waktu_tugas).all()
        return render_template('index.html', konten = tampilkan)

@app.route('/hapus/<int:nomor>')
def hapus(nomor):
    hapus_tugas = Tugasbaru.query.get_or_404(nomor)
    print(hapus_tugas)
    dbku.session.delete(hapus_tugas)
    dbku.session.commit()
    return redirect('/')

@app.route('/edit/<int:nomor>', methods=['POST', 'GET'])
def edit(nomor):
    nomor_tugas = Tugasbaru.query.get_or_404(nomor)
    if request.method == 'POST':
        # nomor_tugas.namatugas = request.form['initugas'] # ini sama saja dengan seperti ini:
        Tugasbaru.query.get_or_404(nomor).namatugas = request.form['initugas']
        dbku.session.commit()
        return redirect('/')
    else:
        return render_template('simpan.html', tugas=nomor_tugas)


if __name__ == '__main__':
    app.run(debug=True)