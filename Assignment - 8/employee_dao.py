import sqlite3
from employee import Employee

class EmployeeDAO:

    def __init__(self, databasename):
        self.__conn = sqlite3.connect(databasename)
        self.__cursor = self.__conn.cursor()
        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS employee (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                position TEXT,
                salary REAL,
                hire_date TEXT
            )
        ''')
        self.__conn.commit()

    def insert(self, employee: Employee):
        sql = '''
            INSERT INTO employee(name, position, salary, hire_date)
            VALUES (?, ?, ?, ?)
        '''
        self.__cursor.execute(sql, (employee.name, employee.position, employee.salary, employee.hire_date))
        self.__conn.commit()
        return self.__cursor.lastrowid

    def get_by_id(self, id):
        sql = 'SELECT * FROM employee WHERE id = ?'
        self.__cursor.execute(sql, (id,))
        row = self.__cursor.fetchone()
        return Employee(*row) if row else None

    def get_all(self):
        sql = 'SELECT * FROM employee'
        self.__cursor.execute(sql)
        rows = self.__cursor.fetchall()
        return [Employee(*row) for row in rows]

    def update(self, employee: Employee):
        sql = '''
            UPDATE employee
            SET name = ?, position = ?, salary = ?, hire_date = ?
            WHERE id = ?
        '''
        self.__cursor.execute(sql, (employee.name, employee.position, employee.salary, employee.hire_date, employee.id))
        self.__conn.commit()
        return self.__cursor.rowcount

    def delete(self, id):
        sql = 'DELETE FROM employee WHERE id = ?'
        self.__cursor.execute(sql, (id,))
        self.__conn.commit()
        return self.__cursor.rowcount
