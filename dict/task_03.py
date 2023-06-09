from random import randint

first_list = []
second_list = []

first_list_length = randint(1, 20)
second_list_length = randint(1, 20)

for i in range(0, first_list_length):
    first_list.append(i)

for i in range(0, second_list_length):
    second_list.append(i)

print(f'First list:\n{first_list} ')
print()
print(f'Second list:\n{second_list}')
print()

common_dict = {}

if len(first_list) >= len(second_list):
    for index in range(len(first_list)):
        if index not in range(len(second_list)):
            common_dict[first_list[index]] = 0
        else:
            common_dict[first_list[index]] = second_list[index] / 2
if len(first_list) < len(second_list):
    for index in range(len(second_list)):
        if index not in range(len(first_list)):
            common_dict[second_list[index]] = 0
        else:
            common_dict[second_list[index]] = first_list[index] / 2

print(f'Common dict:\n{common_dict}')
