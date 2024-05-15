import pymysql
import pymysql.cursors

def get_db():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='pbo2',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection