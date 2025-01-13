class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    @classmethod
    def change_color(cls, new_color):
        cls.color = new_color

first_animal = Animal("Alex", 200)
first_animal.change_color("red")
second_animal = Animal("John", 150)
second_animal.change_color("green")

print(first_animal)