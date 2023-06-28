def convert_to_normal_view(filename):

    with open(filename) as my_file:

        data = my_file.readlines()

        true_data = []

        for string in data:
            if string[-1] == '\n':
                true_data.append(string[:-1])
            else:
                true_data.append(string)

        for string in true_data:
            if string == '':
                true_data.remove(string)

    return true_data


def print_every_second_row(data):
    for i in range(len(data)):
        if i % 2:
            print(data[i])


def print_every_third_row(data):
    for i in range(len(data)):
        if i != 0 and i % 3 == 0:
            print(data[i - 1])


def print_first_four_rows(data):
    if len(data) >= 4:
        for row in range(4):
            print(data[row])
    else:
        for row in range(len(data)):
            print(data[row])


def print_from_to(data, from_row, to_row):
    for i in range(len(data)):
        if from_row - 1 <= i < to_row:
            print(data[i])


def main():
    filename = 'poem.txt'
    data = convert_to_normal_view(filename)

    print_every_second_row(data)

    print_every_third_row(data)

    print_first_four_rows(data)

    print_from_to(data, 3, 6)


if __name__ == '__main__':
    main()
