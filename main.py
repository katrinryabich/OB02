from users import User, Admin

user_daniel = User("Daniel")
user_sandra = User("Sandra")
users_list = Admin.get_userinfo()
print(users_list)
print(user_daniel.get_userinfo())

