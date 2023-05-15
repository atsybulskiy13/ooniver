from random import randint

n = 100
quantity = 10

new_list = [0] * quantity

for i in range(10):
    new_list[i] = randint(0, n)

print(new_list)
print()

sorted_list = []

for elem in range(len(new_list)):
    sorted_list.append(min(new_list))
    new_list.remove(min(new_list))

print(sorted_list)
