from datetime import datetime


class Person:

    def __init__(self, name, height, weight, age):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age

    def birthday(self):
        today = datetime.now()
        if today.month == 6 and today.day == 20:
            self.age += 1


sunshine = Person('Sunshine', 190, 92, 22)

print(sunshine.age)

sunshine.birthday()

print(sunshine.age)
