from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    cari = request.args.get('cari')
    return render_template('index.html', cariitem=cari)

@app.route('/login', methods=['GET', 'POST'])
def fungsilogin():
    if request.method == 'POST':
        respon = make_response('username you adalah ' + request.form['username'])
        respon.set_cookie('user_name', request.form['username'])
        return respon
    
    return render_template('login.html')

@app.route('/cookie')
def lihatcookie():
    username = request.cookies.get('user_name')
    return f"Username yang ada di cookie adalah {username}"