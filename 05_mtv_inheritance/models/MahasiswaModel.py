# models/DosenModels.py
from core.CoreModelMahasiswa import CoreModel

class MahasiswaModel(CoreModel):

    def __init__(self):
        self.table_name = "mahasiswa"
        self.table_id = "id"