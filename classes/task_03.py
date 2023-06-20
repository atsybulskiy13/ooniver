class Person:

    def __init__(self, name, height, weight, age, salary=1000):
        self.name = name
        self.height = height
        self.weight = weight
        self.__age = age
        self.__salary = salary

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            print('Age cannot be < 0')
        else:
            self.__age = age

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary=0):
        if salary:
            self.__salary = salary
        else:
            self.__salary += 100


sunshine = Person('Sunshine', 190, 92, 22)

print(sunshine.get_age())

sunshine.set_age(45)

print(sunshine.get_age())

sunshine.salary = 0

print(sunshine.salary)

sunshine.salary = 2000

print(sunshine.salary)
