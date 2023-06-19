from random import randint

n = 100
quantity = 10

new_list = [0] * quantity

for i in range(10):
    new_list[i] = randint(0, n)

print(new_list)
print()

cycle_flag = True

while cycle_flag:
    cycle_flag = False
    for i in range(len(new_list) - 1):
        if new_list[i] > new_list[i + 1]:
            new_list[i + 1], new_list[i] = new_list[i], new_list[i + 1]
            cycle_flag = True

print('Sorted: ')
print(new_list)
