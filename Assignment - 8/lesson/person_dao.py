import sqlite3
from person import Person

class PersonDao:

    def __init__(self, databasename):
        self.__conn = sqlite3.connect(databasename)
        self.__cursor = self.__conn.cursor()


    def get_all(self):
        sql = 'SELECT * FROM person'
        self.__cursor.execute(sql)

        rows = self.__cursor.fetchall()
        persons = []
        for row in rows:
            p = Person(id=row[0], name=row[1], surname=row[2], email=row[3])
            persons.append(p)

        return persons

    def get_by_id(self, id):
        sql = '''
               SELECT id, name, surname, email
               FROM person
               WHERE id = ?
           '''

        self.__cursor.execute(sql, (id,))

        row = self.__cursor.fetchone()
        if row:
            person = Person(id=row[0], name=row[1], surname=row[2], email=row[3])
        else:
            person = None

        return person


    def insert(self, person:Person):

        sql = '''
            INSERT INTO person(name, surname, email)
            VALUES(?, ? , ?) 
        '''
        self.__cursor.execute(sql, (person.name, person.surname, person.email))
        self.__conn.commit()

        return self.__cursor.lastrowid


    def update(self, person:Person):

        sql = '''
            UPDATE person
            SET name = ?, surname = ?, email=?
            WHERE id = ?
        '''

        self.__cursor.execute(sql, (person.name, person.surname, person.email, person.id))
        self.__conn.commit()

        return self.__cursor.rowcount


    def delete(self, id):
        sql = '''
            DELETE FROM person
            WHERE id = ?
        '''
        self.__cursor.execute(sql, (id,))
        self.__conn.commit()

        return self.__cursor.rowcount



