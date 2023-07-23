from abc import ABC, abstractmethod


class Rescuer(ABC):
    weight = 0
    height = 0
    fatigue = 0
    able_to_work = True

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def change_weight(self, weight=0):
        raise NotImplementedError

    @abstractmethod
    def save(self):
        raise NotImplementedError

    @abstractmethod
    def chill(self):
        raise NotImplementedError

    @abstractmethod
    def change_fatigue(self):
        raise NotImplementedError


class Animals(Rescuer):

    def change_weight(self, weight: float = 0):

        if weight < 0:
            raise ValueError('Weight cannot be < 0')
        else:
            if weight:
                if weight > 0.05:
                    self.weight += 0.05
                else:
                    self.weight += weight
            else:
                self.weight += 0.01

    def change_fatigue(self):
        self.fatigue += 1
        if self.fatigue == 10:
            self.able_to_work = False
            print('Fatigue is 10, need rest')

    def chill(self):
        print('Relax, take it easy...')
        self.fatigue = 0
        self.able_to_work = True

    def save(self):
        if self.able_to_work:
            print('Saving...')
            self.change_fatigue()
        else:
            print('Need to chill')


class Rodents(Animals):

    def run(self):
        if self.able_to_work:
            print('running...')
            self.change_fatigue()
        else:
            print('Need to chill')

    def jump(self):
        if self.able_to_work:
            print('jumping...')
            self.change_fatigue()
        else:
            print('Need to chill')


class Mouse(Rodents):

    weight = 0.3

    def eat_everything(self):
        if self.able_to_work:
            print('Eating...')
            self.change_fatigue()
        else:
            print('Need to chill')


class Chipmunk(Rodents):

    weight = 0.5

    def eat_nuts(self):
        if self.able_to_work:
            print('omnomnom')
            self.change_fatigue()
        else:
            print('Need to chill')


class Fly(Animals):

    weight = 0.01

    def change_weight(self, weight=0):
        if weight < 0:
            raise ValueError('Weight cannot be < 0')
        else:
            self.weight += 0.001

            if self.weight > 0.02:
                print('Cannot fly while weight > 0.02')

    def fly(self):
        if self.able_to_work:
            if self.weight <= 0.02:
                print('I believe i can fly...')
                self.change_fatigue()
            else:
                print('I am too fat(((')
        else:
            print('Need to chill')


vasya = Mouse('Name')
petya = Chipmunk('name2')
grisha = Fly('name3')

vasya.change_weight(0)
print(vasya.weight)
