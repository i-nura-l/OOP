# Parent class
class Person:
   def __init__(self, name, age):
       self.name = name
       self.age = age

   def introduce(self):
       print("Hi, I am a person", self.name)

class Employee(Person):
    def __init__(self, name, age, company, speciality):
        # Call Parent class constructor
        super().__init__(name, age)
        self.company  = company
        self.speciality = speciality

    def introduce(self):
        print("I am", self.speciality, 'work at', self.company)

# Child class inheriting from Person
class Student(Person, Employee):
   def __init__(self, name, age, student_id, email):
       # Call Parent class constructor
       super().__init__(name, age)
       super().__init__(speciality="Ana", company='Uni')
       self.student_id = student_id
       self.email = email

   def introduce(self):
       print(f"Student: My id is {self.student_id}")

   def info(self):
        print("Student of AIU", self.speciality, self.company)



person = Person('Aaaaa', 'Bbbb')
employee = Person('Nur',45, "Data", 'Comp')
student = Student('Cccc', 'Dddd',243, '.com')

person.introduce()

student.introduce()
student.info()
print()
print(issubclass(Student, Employee))