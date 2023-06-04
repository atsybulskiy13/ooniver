import get_data
import menu
import csv_logic


def main():

    menu.show_menu()

    operation = menu.get_user_option()

    match operation:
        case '1':

            csv_logic.print_csv()

            main()

        case '2':

            csv_logic.add_user_in_csv()

            main()

        case '3':

            user = csv_logic.get_user_by_id()
            print(*user)

            main()

        case '4':

            csv_logic.change_user_by_id()

            main()

        case '5':

            csv_logic.delete_user_by_id()

            main()

        case '6':

            users = csv_logic.find_user_by_lastname()

            for user in users:
                print(*user)

            main()

        case '7':

            print('The program finished!')


if __name__ == '__main__':
    main()
