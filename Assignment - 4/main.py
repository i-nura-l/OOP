from user import User
from user_service import UserService
from user_util import UserUtil

if __name__ == '__main__':


    user1 = User(UserUtil.generate_user_id(), 'aa', 'bb', UserUtil.generate_password())
    print(user1.get_details())

    UserService.add_user(User(UserUtil.generate_user_id(), 'bb', 'cc', UserUtil.generate_password()))

    print(UserService.get_number())
