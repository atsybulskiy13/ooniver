from random import randint

numbers = []

for i in range(0, 100):
    numbers.append(randint(10, 100))

print(f'Original list:\n{sorted(numbers)}')
print()
print(f'List without dublicates:\n{sorted(set(numbers))}')
