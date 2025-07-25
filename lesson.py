class Bird():
    def __init__(self,name, color, voice):
        self.name = name
        self.color = color
        self.voice = voice

    def fly(self):
        print(f"{self.name} is flying")

    def eat(self):
        print(f"{self.name} is eating")

    def sing(self):
        print(f"{self.name} is singing - {self.voice}")

    def info(self):
        print(f"{self.name}  - name")
        print(f"{self.color}  - color")
        print(f"{self.voice}  - voice")


class Pigion(Bird):
    def __init__(self,name, color, voice, favourite_food):
        super().__init__(name, color, voice)
        self.favourite_food = favourite_food

    def sing(self):
        print(f"{self.name} is singing kyrlyk-kyrlyk")
    def walk(self):
        print(f"{self.name} is walking")


class Test():
    def public_func(self):
        print("публичный метод")

    def _protected_func(self):
        print("защищенный метод")

    def __private_func(self):
        print("приватный метод")

    def test_private(self):
        self.__private_func()


test = Test()
test.public_func()
test._protected_func()
test.test_private()

bird1 = Pigion("Gosha", "grey", "kyrlyk","hleb")
bird1.sing()
bird1.walk()
bird2 =  Bird("Maska", "white", "chirik")