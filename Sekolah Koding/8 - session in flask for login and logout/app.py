from flask import Flask, render_template, request, make_response, session, url_for, redirect

app = Flask(__name__)
app.secret_key = "nsafskjbfbfjbgsgnagjb34343443/;';d'sd"


@app.route('/')
def index():
    konten = {
        'judul':'ini home bro'
    }
    cari = request.args.get('cari')
    return render_template('index.html', cariitem=cari, varhome = konten)

@app.route('/login', methods=['GET', 'POST'])
def fungsilogin():
    if request.method == 'POST':
        respon = make_response('username you adalah ' + request.form['username'])
        respon.set_cookie('user_name', request.form['username'])
        session['namauser'] = request.form['username']
        return respon
    
    if 'namauser' in session:
        nama = session['namauser']
        return redirect(url_for('fungsiprofil', namakamu1=nama))
    return render_template('login.html')

@app.route('/logout')
def fungsiLogout():
    session.pop('namauser')
    return render_template('login.html')

@app.route('/profil/')
def fungsiprofil():
    namasaya = request.args.get('namakamu1')
    return render_template('profile.html', namaaing = namasaya)

@app.route('/cookie')
def lihatcookie():
    username = request.cookies.get('user_name')
    return f"Username yang ada di cookie adalah {username}"

