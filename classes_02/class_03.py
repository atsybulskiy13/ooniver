class Time:

    def __init__(self, seconds, minutes, hours):

        if seconds > 60:
            new_minutes = seconds // 60
            seconds = seconds % 60
            minutes += new_minutes

        if minutes > 60:
            new_hours = minutes // 60
            minutes = minutes % 60
            hours += new_hours

        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def print_true_time(self):
        print(f'{self.hours}:{self.minutes}.{self.seconds}')


now = Time(hours=100, minutes=100, seconds=100)
now.print_true_time()
