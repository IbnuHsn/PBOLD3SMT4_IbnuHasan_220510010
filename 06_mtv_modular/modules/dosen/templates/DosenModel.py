# models/DosenModels.py
from core.CoreModelDosen import CoreModel

class DosenModel(CoreModel):

    def __init__(self):
        self.table_name = "dosen"
        self.table_id = "id"