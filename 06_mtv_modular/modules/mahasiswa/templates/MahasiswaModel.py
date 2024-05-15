# models/DosenModels.py
from core.CoreModel import CoreModel

class MahasiswaModel(CoreModel):

    def __init__(self):
        self.table_name = "Mahasiswa"
        self.table_id = "id"