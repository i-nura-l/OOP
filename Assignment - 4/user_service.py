from user import User

class UserService:
    # class attribute
    users = {}
    @classmethod
    def add_user(cls, user:User):
        user_id = user.user_id
        cls.users[ user_id ] = user

    @classmethod
    def find_user(cls, user_id):
        return

    @classmethod
    def delete_user(cls, user_id):
        return

    @classmethod
    def update_user(cls, user_id, user_update):
        return

    @classmethod
    def get_number(cls):
        return len(cls.users)
