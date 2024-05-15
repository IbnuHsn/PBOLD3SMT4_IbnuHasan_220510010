from connection import get_db
from interfaces.Mahasiswainterface import *

class MahasiswaModel(Mahasiswainterface):
    
    @staticmethod
    def all():
        connection = get_db()
        cursor = connection.cursor()

        query = "SELECT * FROM mahasiswa" 
        cursor.execute(query)
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results

    @staticmethod
    def find(mahasiswa_id):
        connection = get_db()
        cursor = connection.cursor()

        query = "SELECT * FROM mahasiswa WHERE id = %s LIMIT 1" 
        cursor.execute(query, (mahasiswa_id))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result

    @staticmethod
    def store(mahasiswa_obj):
        connection = get_db()
        cursor = connection.cursor()

        query = "INSERT INTO mahasiswa (nim, nama, prodi) VALUES (%s, %s, %s)" 
        cursor.execute(query, (mahasiswa_obj.nim, mahasiswa_obj.nama, mahasiswa_obj.prodi))

        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def update(mahasiswa_id, mahasiswa_obj):
        connection = get_db()
        cursor = connection.cursor()

        query = "UPDATE mahasiswa SET nim=%s, nama=%s, prodi=%s WHERE id = %s"
        cursor.execute(query, (mahasiswa_obj.nim, mahasiswa_obj.nama,  mahasiswa_obj.prodi, mahasiswa_id))

        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def delete(mahasiswa_id):
        connection = get_db()
        cursor = connection.cursor()

        query = "DELETE FROM mahasiswa WHERE id = %s"
        cursor.execute(query, (mahasiswa_id))

        connection.commit()
        cursor.close()
        connection.close()