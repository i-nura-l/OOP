

class User:
    def __init__(self, user_id, name, surname, email='', password='', birthday=None):
        self.user_id = user_id
        self.name= name
        self.surname = surname
        self.email =  email
        self.password = password
        self.birthday = birthday



    def get_details(self):
        return f"Name: {self.name}, Surname: {self.surname}, Email: {self.email}"

    #def get_age(self):
        #return f"AGe: {self.age:.2f}


