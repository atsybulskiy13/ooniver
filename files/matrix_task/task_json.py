from random import randint
import json


def create_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append([0] * n)

    for row in range(len(matrix)):
        for elem in range(len(matrix[row])):
            random_elem = randint(0, 100)
            matrix[row][elem] = random_elem

    return matrix


file_name = 'matrix_task/matrix.json'


def write_json(matrix, file_name):
    with open(file_name, 'w') as my_file:
        data = json.dumps(matrix)
        my_file.write(data)


def two_replacement(file_name):
    with open(file_name) as my_file:
        raw_data = my_file.read()
        data = json.loads(raw_data)

    for row in range(len(data)):
        for index in range(len(data[row])):
            if not data[row][index] % 2:
                data[row][index] = 0
    return data


matrix = create_matrix(3)
write_json(matrix, file_name)
print(two_replacement(file_name))
