class Rescuer:
    weight = 0.019
    height = 10
    fatigue = 0
    able_to_work = True

    def change_weight(self, weight=0):
        if weight:
            if weight > 0.05:
                self.weight += 0.05
            else:
                self.weight += weight
        else:
            self.weight += 0.01

    def __init__(self, name):
        self.name = name

    def save(self):
        if self.able_to_work:
            print('Saving...')
            self.change_fatigue()
        else:
            print('Need to chill')

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

    def chill(self):
        print('Relax, take it easy...')
        self.fatigue = 0
        self.able_to_work = True

    def change_fatigue(self):
        self.fatigue += 1
        if self.fatigue == 10:
            self.able_to_work = False
            print('Fatigue is 10, need rest')


class Mouse(Rescuer):

    def eat_everything(self):
        if self.able_to_work:
            print('Eating...')
            self.change_fatigue()
        else:
            print('Need to chill')


class Chipmunk(Rescuer):

    def eat_nuts(self):
        if self.able_to_work:
            print('omnomnom')
            self.change_fatigue()
        else:
            print('Need to chill')


class Fly(Rescuer):

    def change_weight(self, weight=0):
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


Vzhik = Fly('Vzhik')
Vzhik.jump()
Vzhik.jump()
Vzhik.jump()
Vzhik.jump()
Vzhik.jump()
Vzhik.jump()
Vzhik.jump()
Vzhik.jump()
Vzhik.jump()
Vzhik.jump()
Vzhik.jump()
Vzhik.jump()
Vzhik.chill()
Vzhik.jump()
Vzhik.jump()
print(Vzhik.fatigue)
