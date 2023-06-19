from random import randint

n = 100
quantity = 10

new_list = [0] * quantity

for i in range(10):
    new_list[i] = randint(0, n)

print(new_list)
print()

sorted_list = []

while len(new_list) > 0:
    min_elem = n  # or min(new_list)
    for elem in new_list:
        if elem < min_elem:
            min_elem = elem

    sorted_list.append(min_elem)
    new_list.remove(min_elem)

print(sorted_list)
