from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/testflask'
dbku = SQLAlchemy(app)

class Tugas(dbku.Model):
    nomor = dbku.Column(dbku.Integer, primary_key=True)
    isitugas = dbku.Column(dbku.String(200), nullable=False)
    tanggal_buat = dbku.Column(dbku.DateTime, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return '<Tugas %s' % self.nomor
    
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        namatugas = request.form['tugasharini']
        tugas_baru = Tugas(isitugas=namatugas)
        dbku.session.add(tugas_baru)
        dbku.session.commit()
        redirect('/')
        
    
    tampilkan = Tugas.query.order_by(Tugas.tanggal_buat).all()
    return render_template('index.html', isinyabro = tampilkan )

if __name__ == '__main__':
    app.run(debug=True)