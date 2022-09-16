from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dblatihan.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'isi random string, apa ajalah, atau buat fungsi generator random secret key sendiri'

dbku = SQLAlchemy(app)
migrate = Migrate(app, dbku)


class Pengguna(dbku.Model):
    idPengguna = dbku.Column(dbku.Integer, primary_key=True)
    namaLengkap = dbku.Column(dbku.String(50), nullable=False)
    namaPengguna = dbku.Column(dbku.String(50), nullable=False)
    kataSandi = dbku.Column(dbku.String(128), nullable=False)
    
    @property
    def password(self):
        raise AttributeError('Password tidak bisa dibaca karena sudah di hashing')
    
    @password.setter
    def password(self, password):
        self.kataSandi = generate_password_hash(password, 'sha256')
        
    def verify_password(self, password):
        return check_password_hash(self.kataSandi, password)

@app.route('/')
def index():
    return 'behr'

@app.route('/login/')
def login():
    return render_template('login.html')
    
@app.route('/daftar', methods=['POST', 'GET'])
def daftar_user():
    if request.method == 'POST':
        nama = request.form['namalengkap']
        username = request.form['username']
        password = request.form['password']
        sandiHash = generate_password_hash(password, 'sha256')
        tambahPengguna = Pengguna(namaLengkap = nama, namaPengguna = username, kataSandi = sandiHash)
        try:
            dbku.session.add(tambahPengguna)
            dbku.session.commit()
            return redirect(url_for('login'))
        except:
            return 'Ada masalah pada saat menyimpan user, kemungkinan pada database'
        
        
    return render_template('daftaruser.html')

@app.route('/datauser/')
def data_user():
    tampilkan = Pengguna.query.all()
    return render_template('datauser.html', konten=tampilkan)
    
if __name__ == '__main__':
    app.run(debug=True)
