from flask import *
from views.MatakuliahView import *

app_matakuliah  =  Blueprint('app_matakuliah', __name__, template_folder='templates')
app_matakuliah.add_url_rule('/', 'index', MatakuliahView().index, methods=['GET'])
app_matakuliah.add_url_rule('/create', 'create', MatakuliahView().create, methods=['GET'])
app_matakuliah.add_url_rule('/edit/<int:matakuliah_id>', 'edit', MatakuliahView().edit, methods=['GET'])
app_matakuliah.add_url_rule('/store', 'store', MatakuliahView().store, methods=['POST'])
app_matakuliah.add_url_rule('/update/<int:matakuliah_id>', 'update', MatakuliahView().update, methods=['POST'])
app_matakuliah.add_url_rule('/delete/<int:matakuliah_id>', 'delete', MatakuliahView().delete, methods=['GET'])