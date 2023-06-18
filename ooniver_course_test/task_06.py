from random import randint
import json

matrix_lenth = int(input('Enter matrix lenth: '))

matrix = []

for list_index in range(matrix_lenth):
    matrix.append([0] * matrix_lenth)

my_dict = {}

for list_index in range(matrix_lenth):

    for elem_imdex in range(matrix_lenth):
        random_elem = randint(0, 9)
        matrix[list_index][elem_imdex] = random_elem
        if list_index == elem_imdex:
            my_dict[f'list_{list_index}'] = matrix[list_index][elem_imdex]

with open('numbers.json', 'w') as my_file:
    data = json.dumps(my_dict, indent=4)
    my_file.write(data)
