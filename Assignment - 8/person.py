
class Person:

    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname


    def __str__(self):
        return f'Id: {self.id} ...'