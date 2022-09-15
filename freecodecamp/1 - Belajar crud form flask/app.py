from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/testflask"
dbku = SQLAlchemy(app)

class Todo(dbku.Model):
    idi = dbku.Column(dbku.Integer, primary_key=True)
    konten = dbku.Column(dbku.String(200), nullable=False)
    tanggal_dibuat = dbku.Column(dbku.DateTime, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return '<Tugas %s' % self.idi
    


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tugasku = request.form['tugasharini']
        tugas_baru = Todo(konten=tugasku)
        
        try:
            dbku.session.add(tugas_baru)
            dbku.session.commit()
            return redirect('/')
        except:
            return 'Ada masalah di database'
    else:
        tugasku = Todo.query.order_by(Todo.tanggal_dibuat).all()
        return render_template('index.html', mytugas = tugasku)


@app.route('/hapus/<int:idtugas>')
def hapus(idtugas):
    try:
        get_id = Todo.query.get_or_404(idtugas)
        dbku.session.delete(get_id)
        dbku.session.commit()
    except:
        return 'Ada masalah di database'
    return redirect('/')

@app.route('/edit/<int:idtugas>', methods=['GET', 'POST'])
def edit(idtugas):
    get_id = Todo.query.get_or_404(idtugas)
    if request.method == 'POST':
        get_id.konten = request.form['tugasharini']
        try:
            dbku.session.commit()
            return redirect('/')
        except:
            return 'ada kesalahan didalam database'
    
    return render_template('edit.html', konten=get_id)







if __name__ == "__main__":
    app.run(debug=True)