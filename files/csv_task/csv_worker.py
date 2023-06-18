import get_data
import menu
import csv_logic


def main():
    menu.show_menu()

    operation = menu.get_user_option()

    match operation:
        case '1':

            csv_logic.print_csv_users()

        case '2':

            csv_logic.add_user_in_csv()

        case '3':

            id = menu.get_user_id()
            user = csv_logic.get_user_by_id(id)
            print(*user)

        case '4':

            id = menu.get_user_id()
            csv_logic.change_user_by_id(id)

        case '5':

            id = menu.get_user_id()
            csv_logic.delete_user_by_id(id)

        case '6':

            users = csv_logic.return_user_by_lastname()

            for user in users:
                print(*user)

        case '7':

            print('The program finished!')
            return

    main()


if __name__ == '__main__':
    main()
