from datetime import datetime


class Person:
    name = 'Sasha'
    height = 190
    weight = 92
    sleeping = False

    def say_hello(self):
        print('Hello!')

    def sleep(self):
        today = datetime.now()
        if today.hour == 13:
            self.sleeping = True

    def get_up(self):
        self.sleeping = False


sasha = Person()

sasha.say_hello()

sasha.sleep()

sasha.get_up()
