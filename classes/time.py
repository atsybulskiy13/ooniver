class Time:
    seconds = 0
    minutes = 0
    hours = 0

    def __init__(self, seconds=0, minutes=0, hours=0):

        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

        self.make_true_time(self.seconds, self.minutes, self.hours)

    def __add__(self, other):
        return Time(self.seconds + other.seconds, self.minutes +
                    other.minutes, self.hours + other.hours)

    def __sub__(self, other):
        return Time(self.seconds - other.seconds, self.minutes -
                    other.minutes, self.hours - other.hours)

    def __gt__(self, other):

        if self.hours * 3600 + self.minutes * 60 + self.seconds >\
                other.hours * 3600 + other.minutes * 60 + other.seconds:
            return True
        else:
            return False

    def __lt__(self, other):

        if self.hours * 3600 + self.minutes * 60 + self.seconds < \
                other.hours * 3600 + other.minutes * 60 + other.seconds:
            return True
        else:
            return False

    def make_true_time(self, seconds, minutes, hours):
        if seconds > 60:
            new_minutes = seconds // 60
            seconds = seconds % 60
            minutes += new_minutes
        if minutes > 60:
            new_hours = minutes // 60
            minutes = minutes % 60
            hours += new_hours

        if seconds < -60:
            seconds += 60
            minutes -= 1
        if minutes < -60:
            minutes += 60
            hours -= 1

        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def print_true_time(self):
        if self.seconds >= 0:
            if self.minutes >= 0:
                if self.hours >= 0:
                    print(f'{self.hours}:{self.minutes}:{self.seconds}')
        else:
            print(f'-{abs(self.hours)}:{abs(self.minutes)}:{abs(self.seconds)}')


now1 = Time(seconds=57, minutes=59, hours=1)
now2 = Time(seconds=58, minutes=59, hours=1)
now3 = now1 + now2

now1.print_true_time()
now2.print_true_time()
now3.print_true_time()

print(now1 > now2)
print(now1 < now2)
print(now3 < now1)
