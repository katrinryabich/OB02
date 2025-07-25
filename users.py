import uuid


class User():
    def __init__(self, name):
        self._id = str(uuid.uuid4())
        self._name = name
        self._access_lvl = "user"


    def set_id(self):
        return self._id

    def __repr__(self):
        return f"(id: {self._id}, name: {self._name}, access level: {self._access_lvl})"


class Admin(User):

    _list_of_users = []

    def __init__(self, name):
        super().__init__(name)
        self._access_lvl = "admin"
        self._list_of_users.append(self)


    def add_user(self, user_name):
        if isinstance (user_name, User):
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
                 return True
        else: print(f"can't find user with id: {id}")

    def __repr__(self):
        return f"(id: {self._id}, name: {self._name}, access level: {self._access_lvl})"

    @classmethod
    def get_users(cls):
        return cls._list_of_users

