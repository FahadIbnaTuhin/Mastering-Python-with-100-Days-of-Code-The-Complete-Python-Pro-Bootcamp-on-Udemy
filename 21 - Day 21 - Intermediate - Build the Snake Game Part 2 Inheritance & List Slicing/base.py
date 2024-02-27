class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breath(self):
        print("Inhale and exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("under the water")

    def swim(self):
        print("I can swim")


nem = Fish()
nem.breath()
