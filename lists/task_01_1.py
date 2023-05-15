from random import randint

n = 100
quantity = 10

new_list = [0] * quantity

for i in range(10):
    new_list[i] = randint(0, n)

print(new_list)
print()

for elem in new_list:
    if not elem % 2:
        print(elem, end=' ')
    if str(elem)[-1] == '7':
        print(elem, end=' ')
