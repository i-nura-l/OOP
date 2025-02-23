from user import User

class UserService:
    # class attribute
    users = {}

    @classmethod
    def add_user(cls, user:User):
        user_id = user.user_id
        cls.users[ user_id ] = user
        print(f"User {user.user_id} added successfully.\n")

    @classmethod
    def find_user(cls, user_id):
        return cls.users.get(user_id, None)

    @classmethod
    def delete_user(cls, user_id):
        if user_id in cls.users:
            del cls.users[user_id]
            print(f"User {user_id} deleted successfully.\n")
        else:
            print(f"User {user_id} not found.\n")

    @classmethod
    def update_user(cls, user_id, **user_update):
        user = cls.find_user(user_id)
        if user:
            for key, value in user_update.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            print(f"User {user_id} updated successfully.\n")
        else:
            print(f"User {user_id} not found.\n")

    @classmethod
    def get_number(cls):
        return len(cls.users)
