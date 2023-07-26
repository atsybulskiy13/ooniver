# flake8: noqa
def show_menu():
    print()
    print('|---------------MENU---------------|')
    print('|----------------------------------|')
    print('| Select an option:                |')
    print('| 1. Show all teams                |')
    print('| 2. Show all players              |')
    print('| 3. Show all players without team |')
    print('| 4. Create new team               |')
    print('| 5. Create new player             |')
    print('| 6. Add player to team            |')
    print('| 7. Remove player from team       |')
    print('| 8. Delete player                 |')
    print('| 8. Delete team                   |')
    print('| 9. Exit                          |')
    print('|----------------------------------|')
    print()


def get_user_option():
    user_option = input('Enter the number of option: ')
    return user_option
