def print_menu():
    print()
    print('| Operations:                        |')
    print('______________________________________')
    print('| 1. Celsius to Fahrenheit           |')
    print('| 2. Miles to kilometers             |')
    print('| 3. Kilometers to meters            |')
    print('| 4. Nautical miles to kilometers    |')
    print('| 5. kilometers to feet              |')
    print('| Enter 6 to finish the program      |')
    print('______________________________________')
    print()


def get_user_operation():
    operation = input('Enter the number of operation: ')
    if operation.isdigit():
        operation1 = int(operation)
        return operation1
    else:
        print("You can enter only digits, try again: ")
        return get_user_operation()


def get_user_value():
    value1 = input('Enter your value: ')
    if value1.isdigit():
        value1 = float(value1)
        return value1
    else:
        print("You can enter only digits, try again: ")
        return get_user_value()


def celsius_to_fahrenheit(celsius: float):
    result = celsius * 1.8 + 32
    return result


def miles_to_kilometers(miles: float):
    result = miles * 1.609
    return result


def kilometers_to_meters(kilometers: float):
    result = kilometers * 1000
    return result


def n_miles_to_kilometers(n_miles: float):
    result = n_miles * 1.852
    return result


def kilometers_to_feet(kilometers: float):
    result = kilometers * 3280.84
    return result


def worker():
    print_menu()

    operation = get_user_operation()

    res = None

    match operation:
        case 1 | 2 | 3 | 4 | 5:
            match operation:
                case 1:
                    value1 = get_user_value()
                    res = celsius_to_fahrenheit(value1)
                case 2:
                    value1 = get_user_value()
                    res = miles_to_kilometers(value1)
                case 3:
                    value1 = get_user_value()
                    res = kilometers_to_meters(value1)
                case 4:
                    value1 = get_user_value()
                    res = n_miles_to_kilometers(value1)
                case 5:
                    value1 = get_user_value()
                    res = kilometers_to_feet(value1)

            print(f'Your result from operation {operation}: {res}')
            worker()

        case 6:
            print('The program finished!')
        case _:
            print('You entered wrong number, try again')
            worker()


def main():
    worker()


if __name__ == '__main__':
    main()
