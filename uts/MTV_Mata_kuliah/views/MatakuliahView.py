from flask import *
from models.MatakuliahModel import *

class MatakuliahView:

    @staticmethod
    def index():
        data = MatakuliahModel().all()
        return render_template('matakuliah_index.html', data=data)
    
    @staticmethod
    def create():
        return render_template('matakuliah_create.html')
    
    @staticmethod
    def store():
        matakuliah_obj = MatakuliahModel()
        post = request.form
        matakuliah_obj.kodematakuliah = post['kodematakuliah']
        matakuliah_obj.matakuliah = post['matakuliah']
        matakuliah_obj.dosen = post['dosen']
        matakuliah_obj.jumlahsks = post['jumlahsks']
        MatakuliahModel.store(matakuliah_obj)
        return redirect('/matakuliah')
    
    @staticmethod
    def edit(matakuliah_id):
        obj = MatakuliahModel().find(matakuliah_id)
        return render_template('matakuliah_edit.html', obj=obj)

    @staticmethod
    def update (matakuliah_id):
        data = MatakuliahModel.find(matakuliah_id)
        if data:
            post = request.form
            matakuliah_obj = MatakuliahModel()
            matakuliah_obj.kodematakuliah = post['kodematakuliah']
            matakuliah_obj.matakuliah = post['matakuliah']
            matakuliah_obj.dosen = post['dosen']
            matakuliah_obj.jumlahsks = post['jumlahsks']
            MatakuliahModel.update(matakuliah_id, matakuliah_obj)
            return redirect('/matakuliah')
        else:
            return redirect(request.referrer)

    @staticmethod
    def delete(matakuliah_id):
        data = MatakuliahModel.find(matakuliah_id)
        if data:
            MatakuliahModel.delete(matakuliah_id)
            return redirect('/matakuliah/')
        else:
            return redirect(request.referrer)