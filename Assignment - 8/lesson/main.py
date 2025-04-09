import sqlite3
from person import Person
from person_dao import PersonDao


if __name__ == '__main__':

    dao = PersonDao('data.sqlite')

    persons = dao.get_all()
    p = Person(id=1, name='HI', surname='NO', email='ddd.cc@mail.com')
    row = dao.update(p)

    dao.insert(p)
    dao.delete(23)

    persons = dao.get_all()
    for per in persons:
        print(per)


