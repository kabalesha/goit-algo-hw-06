class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    def how_many_persons(self):
        print(f"Кількість людей зараз {Person.count}")


first = Person('Boris')
first.how_many_persons()
second = Person('Alex')
first.how_many_persons()

'''
Додамо в клас Animal змінну класу color, значення якої спочатку
дорівнює 'white', і метод change_color, який повинен змінювати 
значення змінної класу color.

Створіть екземпляри об'єкта: first_animal та second_animal

Викличте функцію change_color("red") для будь-якого екземпляра 
об'єкту Animal та змініть значення змінної класу color на "red".
'''