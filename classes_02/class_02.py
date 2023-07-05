class Pet:
    legs = 4

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def voice(self):
        pass

    def legs_quantity(self):
        print(self.legs)


class Cat(Pet):
    def voice(self):
        print('Meoowwwww')


class Parrot(Pet):
    legs = 2
    wings = 2

    def voice(self):
        print('Kar-kar')

    def legs_cout(self, amount):
        if amount == 1:
            print(self.legs)
        elif amount == 2:
            print(super().legs)


cat = Cat('Kanabis', 'male')

print(cat.name, cat.gender)

cat.voice()

cat.legs_quantity()

parrot = Parrot('Kokos', 'male')

print(parrot.name, parrot.gender)

parrot.voice()

parrot.legs_quantity()

parrot.legs_cout(1)
