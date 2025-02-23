import random
from datetime import datetime
import re
import string

class UserUtil:

    @staticmethod
    def generate_user_id():
        two_d = datetime.now().year // 100
        seven_d = random.randint(1000000, 9999999)
        return int(f"{two_d}{seven_d}")

    '''
    @staticmethod
    def generate_password(name, surname, birthday):

        min_l = 8
        special_char = random.choice(string.punctuation)
        password = f'{name.upper()}{surname[0].lower()}{birthday[0]}{special_char}'

        while True:
            if UserUtil.is_strong_password(password):
                return password    
    '''

    def generate_password():
        chars = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = ''.join(random.choices(chars, k=8))
            if UserUtil.is_strong_password(password):
                return password

    @staticmethod
    def is_strong_password(password):
        return (
                len(password) >= 8 and
                any(c.islower() for c in password) and
                any(c.isupper() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in '!@#$%^&*()-_=+[]{}|;:,.<>?/' for c in password)
        )

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@gmail{domain}"

    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-Z]+\.[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$"
        return bool(re.match(pattern, email))