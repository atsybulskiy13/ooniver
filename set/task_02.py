from random import randint

first_list = []
second_list = []

for i in range(10):
    first_list.append(randint(0, 9))
    second_list.append(randint(0, 9))


print(f'Original first list: {first_list}')
print(f'Original second list: {second_list}')
print()

first_list_unics = set(first_list).difference(set(second_list))

second_list_unics = set(second_list).difference(set(first_list))

unics = set(first_list).intersection(set(second_list))

different_elements = list(first_list_unics)

for i in second_list_unics:
    different_elements.append(i)

print(f'Numbers only from first list: {first_list_unics}')
print(f'Numbers only from second list: {second_list_unics}')
print(f'Numbers from both lists: {unics}')
print(f'Different numbers from both lists: {different_elements}')
