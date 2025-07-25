class User():
    def __init__(self, id, name, access_lvl):
        self.id = id
        self.name = name
        self.access_lvl = access_lvl


class Admin(User):
    def __init__(self):
        