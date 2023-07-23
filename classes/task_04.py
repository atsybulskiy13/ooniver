class Rescuer:

    def __init__(self, name):
        self.name = name

    def save(self):
        print('Saving...')

    def chill(self):
        print('Relax, take it easy...')


class Mouse(Rescuer):

    def eat_everything(self):
        print('Eating...')

    def jump(self):
        print('jumping...')

    def run(self):
        print('running...')


class Chipmunk(Rescuer):

    def eat_nuts(self):
        print('omnomnom')

    def jump(self):
        print('jumping...')

    def run(self):
        print('running...')


class Fly(Rescuer):

    def fly(self):
        print('I believe i can fly...')

    def jump(self):
        print()


Chip = Chipmunk('Chip')
Dale = Chipmunk('Dale')
Gaechka = Chipmunk('Gaechka')
Rocky = Mouse('Rocky')
Vzhik = Fly('Vzhik')

Chip.chill()
Chip.eat_nuts()
Dale.jump()
Dale.eat_nuts()
Gaechka.save()
Gaechka.eat_nuts()
Rocky.eat_everything()
Rocky.run()
Vzhik.fly()
Vzhik.chill()
