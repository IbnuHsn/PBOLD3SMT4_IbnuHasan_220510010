from connection import get_db
from interfaces.MatakuliahInterface import *

class MatakuliahModel():
       
    @staticmethod
    def all():
        connection = get_db()
        cursor = connection.cursor()

        query = "SELECT * FROM matakuliah" 
        cursor.execute(query)
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results

    @staticmethod
    def find(matakuliah_id):
        connection = get_db()
        cursor = connection.cursor()

        query = "SELECT * FROM matakuliah WHERE id = %s LIMIT 1" 
        cursor.execute(query, (matakuliah_id))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result

    @staticmethod
    def store(matakuliah_obj):
        connection = get_db()
        cursor = connection.cursor()

        query = "INSERT INTO matakuliah (kodematakuliah, matakuliah, dosen, jumlahsks) VALUES (%s, %s, %s, %s)" 
        cursor.execute(query, (matakuliah_obj.kodematakuliah, matakuliah_obj.matakuliah, matakuliah_obj.dosen, matakuliah_obj.jumlahsks))

        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def update(matakuliah_id, matakuliah_obj):
        connection = get_db()
        cursor = connection.cursor()

        query = "UPDATE matakuliah SET kodematakuliah=%s, matakuliah=%s, dosen=%s,  jumlahsks=%s WHERE id = %s"
        cursor.execute(query, (matakuliah_obj.kodematakuliah, matakuliah_obj.matakuliah, matakuliah_obj.dosen, matakuliah_obj.jumlahsks, matakuliah_id))

        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def delete(matakuliah_id):
        connection = get_db()
        cursor = connection.cursor()

        query = "DELETE FROM matakuliah WHERE id = %s"
        cursor.execute(query, (matakuliah_id))

        connection.commit()
        cursor.close()
        connection.close()