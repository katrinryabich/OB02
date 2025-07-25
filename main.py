from users import User, Admin


admin_natali = Admin("Natali")
admin_alex = Admin("Alex")
user_daniel = User("Daniel")
user_sandra = User("Sandra")
admin_natali.add_user(user_sandra)
admin_natali.add_user(user_daniel)
admin_natali.delete_user("derwwgegeterw")



print(user_daniel)
print(admin_natali.get_userinfo())
admin_natali.delete_user(user_daniel.set_id())
print(admin_alex.get_userinfo())
print(Admin.get_users())

