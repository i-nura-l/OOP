import sqlite3
from person import Person
from person_dao import PersonDao


if __name__ == '__main__':

    dao = PersonDao('data.sqlite')

    persons = dao.get_all()

