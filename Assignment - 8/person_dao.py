import sqlite3

class PersonDao:
    def __init__(self, data):
        self.conn =  sqlite3.connect(data)
        self.__cursor = self.__conn.cursor()


    def get_all(self):
        sql = 'SELECT * FROM person'
        self.__cursor.execute(sql)
        rows = self.__cursor.fetchall()
        persons = []
        for row in rows:
            print(row)

        return persons