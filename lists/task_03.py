from random import randint

n = 100

rows_quantity = 3
elements_quantity = 3

matrix = []

for i in range(rows_quantity):
    matrix.append([0] * elements_quantity)

for row in range(len(matrix)):
    for elem in range(len(matrix[row])):
        matrix[row][elem] = randint(0, n)

print(matrix)

min_element = n
max_element = 0

for row in range(len(matrix)):
    for elem in matrix[row]:
        if elem > max_element:
            max_element = elem
        if elem < min_element:
            min_element = elem

print('Max element in matrix = ', max_element)
print('Min element in matrix = ', min_element)
