from random import randint

first_list = []
second_list = []

for i in range(0, randint(1, 20)):
    first_list.append(i)

for i in range(0, randint(1, 20)):
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
        elif first_list[index] == 0:
            common_dict[first_list[index]] = second_list[index]
        else:
            common_dict[first_list[index]] = second_list[index] / 2
if len(first_list) < len(second_list):
    for index in range(len(second_list)):
        if index not in range(len(first_list)):
            common_dict[second_list[index]] = 0
        elif second_list[index] == 0:
            common_dict[second_list[index]] = first_list[index]
        else:
            common_dict[second_list[index]] = first_list[index] / 2

print(f'Common dict:\n{common_dict}')
