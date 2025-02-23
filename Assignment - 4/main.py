from user import User
from user_service import UserService
from user_util import UserUtil

if __name__ == '__main__':


    user1 = User(UserUtil.generate_user_id(), 'Nurali', 'Bakytbek', (2005, 8, 22))
    print(user1.get_details())
    print(user1.get_age())

    user2 = User(5, "Jane", "Smith", (1995, 8, 20))

    UserService.add_user(User(UserUtil.generate_user_id(), 'Nura', 'Bakyt', UserUtil.generate_password()))
    UserService.add_user(user1)
    UserService.add_user(user2)

    found_user = UserService.find_user(1)
    print('\n', found_user.get_details() if found_user else "User not found.")

    print(UserService.find_user(5).get_details())
    UserService.update_user(5, email="new.john.doe@example.com")
    print('\n', UserService.find_user(5).get_details())

    UserService.delete_user(2)
    UserService.delete_user(5)

    print(UserService.find_user(5).get_details() if UserService.find_user(5) else "User not found.\n")

    print("\nTotal Users:", UserService.get_number())