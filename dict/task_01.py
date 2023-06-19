from random import randint

my_dict = {}

for index in range(10):
    key = randint(10, 100)
    my_dict[key] = key ** 3

print(f'Original dict - {my_dict}')

for key, value in my_dict.copy().items():
    if not value % 2:
        del my_dict[key]

print(f'Edited dict - {my_dict}')
print()

keys_list = []
values_list = []

for key, value in my_dict.items():
    keys_list.append(key)
    values_list.append(value)

print(f'Keys list - {keys_list}')
print(f'Values list - {values_list}')
print()

sort_flag = True

while sort_flag:
    sort_flag = False
    for index in range(len(keys_list) - 1):  # сделал в одном цикле специально потому, что длина списков одинаковая
        if keys_list[index] < keys_list[index + 1]:
            keys_list[index], keys_list[index + 1] = keys_list[index + 1], keys_list[index]
            sort_flag = True
        if values_list[index] < values_list[index + 1]:
            values_list[index], values_list[index + 1] = values_list[index + 1], values_list[index]
            sort_flag = True

print(f'Sorted keys list - {keys_list}')
print(f'Sorted values list - {values_list}')
