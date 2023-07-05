class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Sashka(Person):
    pass


sasha = Sashka('Sasha')

print(sasha.name)
