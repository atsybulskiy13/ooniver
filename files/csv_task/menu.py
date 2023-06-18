def show_menu():
    print()
    print('|==========================|')
    print('|========== Menu ==========|')
    print('|1. Show users             |')
    print('|2. Add new user           |')
    print('|3. Find user by id        |')
    print('|4. Change user by id      |')
    print('|5. Delete by id           |')
    print('|6. Filter by lastname     |')
    print('|7. Exit                   |')
    print('|==========================|')
    print()


def get_user_option():
    option = input("Enter the number of option you'd like to do: ")
    match option:
        case '1' | '2' | '3' | '4' | '5' | '6' | '7':
            return option
        case _:
            print('You entered wrong operation number!')
            return get_user_option()


def get_user_id():

    id = input('Enter user id: ')

    if id.isdigit():
        return id
    else:
        print('Id should contain only digits!')
        return get_user_id()
