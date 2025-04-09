
class Person:

    def __init__(self, id, name, surname, email):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email

    def __str__(self):
        return f'Id: {self.id}, Name: {self.name}, Surname: {self.surname}'