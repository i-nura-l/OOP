class Person:  # is templete how

    # constructor - special method to initialize attributes
    def __init__(self, name, surname, age=None, gender=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    # methods
    def walk(self):
        print('Person', self.name, self.surname, 'is walking.')

    def info(self):
        print('Person name', self.name, 'surname', self.surname, 'is', self.age, 'years old.', 'Gender:', self.gender)