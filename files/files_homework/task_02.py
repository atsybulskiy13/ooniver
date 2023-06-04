from task_01 import convert_to_normal_view


def get_user_choice():

    choice = input('Enter row number: ')

    if choice.isdigit():
        return int(choice)
    else:
        return get_user_choice()


def print_full_file(data):
    for row in data:
        print(row)


def print_row(data, row):
    print(data[row - 1])


def main():

    filename = 'poem.txt'

    data = convert_to_normal_view(filename)

    max_row = len(data)

    choice = get_user_choice()

    if choice > max_row:

        print(f'There is no row number {choice} in the file, try again!')
        main()

    else:

        match choice:
            case 0:
                print_full_file(data)
            case _:
                print_row(data, choice)


if __name__ == '__main__':
    main()
