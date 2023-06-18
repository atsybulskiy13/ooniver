from random import randint

lenth = int(input('Enter lenth: '))

random_list = []

for i in range(lenth):
    random_num = randint(0, 100)
    random_list.append(random_num)

max_number = min_number = random_list[0]

for number in random_list:
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

my_dict = {'min': min_number, 'max': max_number}

for key, value in my_dict.items():
    print(key, value)
