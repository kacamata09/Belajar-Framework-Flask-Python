from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dblatihan.db'
app.config['SECRET_KEY'] = 'isi random string, apa ajalah, atau buat fungsi generator random secret key sendiri'

dbku = SQLAlchemy(app)


class Pengguna(dbku.Model):
    idPengguna = dbku.Column(dbku.Integer, primary_key=True)
    namaLengkap = dbku.Column(dbku.String(50), nullable=False)
    namaPengguna = dbku.Column(dbku.String(50), nullable=False)
    kataSandi = dbku.Column(dbku.String(128), nullable=False)
    
    @property
    def password(self):
        raise AttributeError('Password tidak bisa dibaca')
    
    @password.setter
    def password(self, password):
        self.kataSandi = generate_password_hash(password)
        
    def verify_pasword(self, password):
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
        tambahPengguna = Pengguna(namaLengkap = nama, namaPengguna = username, kataSandi = password)
        try:
            dbku.session.add(tambahPengguna)
            dbku.session.commit()
            return redirect(url_for('login'))
        except:
            return 'Ada masalah pada saat menyimpan user, kemungkinan pada database'
        
        
    return render_template('daftaruser.html')
    
if __name__ == '__main__':
    app.run(debug=True)
