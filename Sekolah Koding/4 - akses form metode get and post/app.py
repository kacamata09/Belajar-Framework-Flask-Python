from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    cari = request.args.get('cari')
    idyou = request.args.get('idkamu')
    if not cari:
        return render_template('index.html')
    
    return f'<h1>hasil pencarian adalah {cari} dan id you {idyou} </h1>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Ini adalah POST broooooooooo ' + request.form['username']
    
    return render_template('login.html')