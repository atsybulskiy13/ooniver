from random import randint


def create_matrix(rows_number: int, elements_in_rows=randint(0, 9)):
    matrix = []
    for i in range(rows_number):
        matrix.append([0] * elements_in_rows)

    for row in range(len(matrix)):
        for elem in range(len(matrix[row])):
            random_elem = randint(0, 100)
            matrix[row][elem] = random_elem
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def summ(*args):
    s = 0
    for elem in args:
        s += elem
    return s


def sum_and_index(*args):
    s = 0
    for elem in range(len(args)):
        s = s + elem * args[elem]
    return s


def kwargs_practice(**kwargs):
    for key, value in kwargs.items():
        if not len(key) % 2:
            print(key, value)


my_dict = {
    'asasd': 'Vasya',
    'asdf': 'Petya',
    'asdsada': 'Kolya',
    'asdddf': 'Nikita'
}
kwargs_practice(**my_dict)


def get_params(*args, **kwargs):
    if kwargs['action'] == '+':
        result = summa(*args)
        print(result)
    elif kwargs['action'] == '*':
        result = multiply(*args)
        print(result)
    else:
        print('There is no kwargs params')


def summa(*args):
    summ = 0
    for i in args:
        summ += i
    return summ


def multiply(*args):
    multi = 1
    for i in args:
        multi *= i
    return multi


get_params(3, 4, 5, action='+')
get_params(3, 4, 5, action='*')
get_params(3, 4, 5, action='-')
