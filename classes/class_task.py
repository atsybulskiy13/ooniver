from datetime import datetime


class Person:
    name: str
    age: int

    def __init__(self, name='NoName', age=0):
        self.__name = name
        self.age = age

    def __str__(self):
        return f'Name - {self.name}, age - {self.age}'

    def birthday(self):
        today = datetime.now()
        if today.day == 19 and today.month == 6:
            self.age += 1


chel = Person('Sania', 22)

chel.birthday()

print(chel.name)

chel.me = True

print(chel.me)
