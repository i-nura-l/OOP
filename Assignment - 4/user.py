from datetime import datetime
from user_util import UserUtil

class User:
    def __init__(self, user_id: int, name, surname, birthday=None, email=None, password=None):
        self.user_id = user_id
        self.name= name
        self.surname = surname
        self.email = email#UserUtil.generate_email(name, surname, '.com')
        self.password = password#UserUtil.generate_password()
        self.birthday = birthday


    def get_details(self):
        return f"User ID: {self.user_id}\nName: {self.name} {self.surname}\nBirthday: {self.birthday} \nPassword: {self.password}\nEmail: {self.email}"

    def get_age(self):
        today = datetime.today()
        age = today.year - self.birthday[0]
        if today.month < self.birthday[1] or (today.month == self.birthday[1] and today.day < self.birthday[2]):
            age -= 1
        return age


