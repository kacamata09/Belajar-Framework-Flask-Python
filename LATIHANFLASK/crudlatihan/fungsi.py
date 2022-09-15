import mysql.connector


dbku = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='crudlatihanflask'
)

def tambah(db):
    nama = input('Masukkan namamu bro : ')
    nim = int(input('Nim mu apa bro : '))
    alamat = input('Alamat mu dimana bro : ')
    mahasiswa = nama, nim, alamat
    sqlnyabro = 'insert into mahasiswa values(%s, %s, %s)'
    cursorbro = db.cursor()
    cursorbro.execute(sqlnyabro, mahasiswa)
    db.commit()
    
def tampilkan(db):
    sqlnya = 'select * from mahasiswa'
    cursor = db.cursor()
    cursor.execute(sqlnya)
    hasil = cursor.fetchall()
    
    if cursor.rowcount == 0:
        print('tak ada date a')
    else:
        for i in hasil:
            print(i)

