from random import randint

n = 100
quantity = 10

new_list = [0] * quantity

for i in range(10):
    new_list[i] = randint(0, n)

print(new_list)
print()

print("Max element = ", max(new_list))
print("Min element = ", min(new_list))
