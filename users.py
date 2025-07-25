import uuid


class User():
    def __init__(self, name):
        self._id = str(uuid.uuid4())
        self._name = name
        self._access_lvl = "user"


    def get_userinfo(self):
        return f"(id: {self._id}, name: {self._name}, access level: {self._access_lvl})"


class Admin(User):
    def __init__(self, name):
        super().__init__(self, name)
        self._access_lvl = "admin"
        self._list_of_users = []

    def add_user(self, user_name):
        if isinstance(user_name, User):
            new_user = user_name
        else:
            new_user = User(user_name)

        self._list_of_users.append(new_user)
        print("user added")

    def delete_user(self, id):
        for i, user in enumerate(self._list_of_users):
            if user._id == id:
                 self._list_of_users.pop(i)
                 print("user deleted")
            else: print(f"can't find user with id: {id}")


    def get_userinfo(self):
        return self._list_of_users



