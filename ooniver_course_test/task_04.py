from random import randint

lenth = int(input('Enter lenth: '))

random_list = []

min_number = 100
max_number = 0

for i in range(lenth):
    random_num = randint(0, 100)
    random_list.append(random_num)
    if random_num > max_number:
        max_number = random_num
    if random_num < min_number:
        min_number = random_num


my_dict = {'min': min_number, 'max': max_number}

for key, value in my_dict.items():
    print(key, value)
