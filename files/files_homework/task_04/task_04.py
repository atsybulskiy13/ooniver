def menu():
    print()
    print('|========================|')
    print('|        Menu            |')
    print('|1. Record new file      |')
    print('|2. Append existing file |')
    print('|========================|')
    print()


def get_user_choice():
    user_choice = input('Please, enter the number of operation: ')

    match user_choice:

        case '1' | '2':

            return user_choice

        case _:

            print('You entered wrong number, please, enter 1 or 2')

            return get_user_choice()


def get_user_string():
    user_string = input('Please enter your string: ')

    return user_string


def create_file(file_name):
    with open(file_name, 'w'):
        pass


def read_file(file_name):
    with open(file_name) as my_file:
        file_data = my_file.read()

    return file_data


def write_data_in_file(file_name, file_data):
    with open(file_name, 'w') as my_file:
        my_file.writelines(file_data)


def add_string_to_file_data(file_name, user_string):
    file_data = read_file(file_name)

    if file_data == '':

        file_data = file_data + user_string

    else:

        file_data = file_data + '\n' + user_string

    return file_data


def write_string_in_file(file_name, user_string):
    new_file_data = add_string_to_file_data(file_name, user_string)

    write_data_in_file(file_name, new_file_data)


def append_file(file_name, user_string):
    with open(file_name, 'a') as my_file:
        my_file.writelines('\n' + user_string)


def worker(user_choice, file_name):
    user_string = get_user_string()

    match user_choice:

        case '1':

            if user_string != '/стоп':
                write_string_in_file(file_name, user_string)
                worker(user_choice, file_name)
            else:
                print('Program finished!')

        case '2':

            if user_string != '/стоп':
                append_file(file_name, user_string)
                worker(user_choice, file_name)
            else:
                print('Program finished!')


def main():
    filename = 'text.txt'

    menu()

    user_choice = get_user_choice()

    match user_choice:
        case '1':
            create_file(filename)
            worker(user_choice, filename)

        case '2':
            worker(user_choice, filename)


if __name__ == '__main__':
    main()
