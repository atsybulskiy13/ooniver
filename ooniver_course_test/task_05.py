from random import randint

matrix_lenth = int(input('Enter matrix lenth: '))

matrix = []

for list_index in range(matrix_lenth):
    matrix.append([0] * matrix_lenth)

for list_index in range(matrix_lenth):
    for elem_imdex in range(matrix_lenth):
        random_elem = randint(0, 9)
        matrix[list_index][elem_imdex] = random_elem
        if list_index == elem_imdex:
            print(matrix[list_index][elem_imdex], end=' ')
