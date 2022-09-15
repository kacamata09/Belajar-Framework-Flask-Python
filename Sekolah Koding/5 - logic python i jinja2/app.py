from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    cari = request.args.get('cari')
    return render_template('index.html', cariitem=cari)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Ini adalah POST broooooooooo ' + request.form['username']
    
    return render_template('login.html')