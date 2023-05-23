from random import randint


def create_matrix(rows_number: int, elements_in_rows: int):
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


def find_min_max(matrix):
    min_element = matrix[0][0]
    max_element = matrix[0][0]

    for row in range(len(matrix)):
        for elem in matrix[row]:
            if elem > max_element:
                max_element = elem
            if elem < min_element:
                min_element = elem

    return min_element, max_element


def sort_matrix_ascending(matrix):
    last_elem_in_row = len(matrix[0]) - 1

    sort_flag = True

    while sort_flag:
        sort_flag = False
        for index in range(len(matrix)):  # берем индекс списка из матрицы
            for number in range(len(matrix[index]) - 1):  # берем индекс элемента в списке по индексу(index)
                if matrix[index][number] > matrix[index][number + 1]:
                    matrix[index][number], matrix[index][number + 1] = matrix[index][number + 1], matrix[index][number]
                    sort_flag = True
        for index in range(len(matrix) - 1):
            if matrix[index][last_elem_in_row] > matrix[index + 1][0]:
                matrix[index][last_elem_in_row], matrix[index + 1][0] = matrix[index + 1][0], matrix[index][
                    last_elem_in_row]
                sort_flag = True


def sort_matrix_descending(matrix):
    last_elem_in_row = len(matrix[0]) - 1

    sort_flag = True

    while sort_flag:
        sort_flag = False
        for index in range(len(matrix)):  # берем индекс списка из матрицы
            for number in range(len(matrix[index]) - 1):  # берем индекс элемента в списке по индексу(index)
                if matrix[index][number] < matrix[index][number + 1]:
                    matrix[index][number], matrix[index][number + 1] = matrix[index][number + 1], matrix[index][number]
                    sort_flag = True
        for index in range(len(matrix) - 1):
            if matrix[index][last_elem_in_row] < matrix[index + 1][0]:
                matrix[index][last_elem_in_row], matrix[index + 1][0] = matrix[index + 1][0], matrix[index][
                    last_elem_in_row]
                sort_flag = True


def if_square_matrix(matrix):
    rows_quantity = len(matrix)
    elem_in_row = len(matrix[0])
    if rows_quantity == elem_in_row:
        print('Matrix is square!')
    else:
        print('Matrix is not square!')


def main():
    matrix1 = create_matrix(5, 5)
    print_matrix(matrix1)
    print()
    min_matrix, max_matrix = find_min_max(matrix1)
    print(f'Min matrix element: {min_matrix}')
    print(f'Max matrix element: {max_matrix}')
    print()
    sort_matrix_ascending(matrix1)
    print_matrix(matrix1)
    print()
    sort_matrix_descending(matrix1)
    print_matrix(matrix1)
    print()
    if_square_matrix(matrix1)


if __name__ == '__main__':
    main()
