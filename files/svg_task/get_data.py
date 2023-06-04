from InquirerPy import inquirer


def get_user_data():
    name = input('Enter your name: ').lower()
    last_name = input('Enter your last name: ').lower()
    age = input('Enter your age: ')
    user_data = [name, last_name, age]
    return user_data
