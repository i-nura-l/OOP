class Employee:

    def __init__(self, id, name, position, salary, hire_date):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.hire_date = hire_date

    def __str__(self):
        return (f"Id: {self.id}, Name: {self.name}, "
                f"Position: {self.position}, Salary: {self.salary}, "
                f"Hire Date: {self.hire_date}")
