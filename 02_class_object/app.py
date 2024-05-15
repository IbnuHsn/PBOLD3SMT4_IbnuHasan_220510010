from flask import Flask, render_template

app = Flask(__name__)

class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

class Dosen:
    def __init__(self, nidn, nama, spesialis):
        self.nidn = nidn
        self.nama = nama
        self.spesialis = spesialis
    
@app.route("/one")
def one_object():
    mhs = Mahasiswa('111','John')
    dsn = Dosen('111','Agung', 'Rekayasa Peranngkat lunak')
    return render_template('one_object.html', mhs = mhs, dsn = dsn)

@app.route("/many")
def many_object():
    mhs = [
            Mahasiswa('111', 'John'),
            Mahasiswa('222', 'Wick'),
            Mahasiswa('333', 'Candra'),
            Mahasiswa('444', 'Deden'),
            Mahasiswa('555', 'Endra')
    ]
    dsn = [
            Dosen('111', 'Agung' , 'Rekayasa Perangkat Lunak'),
            Dosen('222', 'Bobon', 'Jaringan Komputer'),
            Dosen('333', 'Candra', 'Sains Data'),
            Dosen('444', 'Deden', 'Pemrograman Mobile'),
            Dosen('555', 'Endra', 'Basis Data')
    ]

    return render_template('many_object.html',mhs = mhs, dsn = dsn)