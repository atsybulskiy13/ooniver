def get_simple_numbers_in_number(number):
    numbers = []
    for number in range(2, number + 1):
        for i in range(2, number):
            if not number % i:
                break
        else:
            numbers.append(number)

    return numbers
