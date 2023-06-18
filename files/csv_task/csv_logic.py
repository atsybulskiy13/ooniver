import csv
from files.csv_task import get_data
import menu

table_head = ['id', 'name', 'last_name', 'age']


def get_users_from_csv():
    users = []

    with open('users.csv') as users_file:
        csv_reader = csv.reader(users_file)

        for row in csv_reader:

            users.append(row)

    return users[1::]


def write_scv(users):
    with open('users.csv', 'w') as users_file:

        csv_writer = csv.writer(users_file)

        if users[0][0] == 'id':
            csv_writer.writerows(users)
        else:
            csv_writer.writerow(table_head)
            csv_writer.writerows(users)


def add_user_in_csv():
    user = get_data.get_user_data()

    last_id = get_last_user_id()

    users = get_users_from_csv()

    user.insert(0, last_id + 1)

    users.append(user)

    write_scv(users)


def get_last_user_id():
    rows = []

    with open('users.csv') as users_file:

        csv_reader = csv.reader(users_file)

        for row in csv_reader:
            rows.append(row)

        if csv_reader.line_num == 0:
            last_id = 0
        else:
            if rows[-1] == table_head:
                last_id = 0
            else:
                last_row = rows[-1]
                last_id = int(last_row[0])

    return last_id


def get_user_by_id(id):
    users = get_users_from_csv()

    for user in users:
        if user[0] == id:
            return user


def delete_user_by_id(id):
    users = get_users_from_csv()

    for user in users:
        if user[0] == str(id):
            users.remove(user)

    write_scv(users)


def change_user_by_id(id):
    users = get_users_from_csv()

    for user in users:
        if user[0] == str(id):
            user[1] = input('Enter new user name: ')
            user[2] = input('Enter new user lastname: ')
            user[3] = input('Enter new user age: ')

    write_scv(users)


def return_user_by_lastname():
    users = get_users_from_csv()

    lastname = input("Enter user's lastname: ")

    found_users = []

    for user in users:
        if user[2].lower() == lastname.lower():
            found_users.append(user)

    return found_users


def print_csv_users():
    users = get_users_from_csv()

    for user in users:
        print(*user)
