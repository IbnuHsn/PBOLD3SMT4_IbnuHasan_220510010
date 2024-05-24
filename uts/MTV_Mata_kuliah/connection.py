import pymysql
import pymysql.cursors

def get_db():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='akademik',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection