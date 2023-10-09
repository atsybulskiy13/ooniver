def get_simple_numbers_in_number(number):
    numbers = []
    for number in range(2, number + 1):
        for i in range(2, number):
            if not number % i:
                break
        else:
            numbers.append(number)

    return numbers


def if_palindrom(string: str):

    splited_string = string.split()

    join_string = ''.join(splited_string)

    new_string = ''

    for char in join_string:
        new_string = char + new_string

    if new_string == join_string:
        return True
    else:
        return False
