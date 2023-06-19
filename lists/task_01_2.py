from random import randint

n = 100
quantity = 10

new_list = [0] * quantity

for i in range(10):
    new_list[i] = randint(0, n)

print(new_list)
print()

max_elem = 0
min_elem = n

for elem in new_list:
    if elem > max_elem:
        max_elem = elem
    if elem < min_elem:
        min_elem = elem

print("Max element = ", max_elem)
print("Min element = ", min_elem)
