number = 2

while number < 101:
    i = 2
    while i < number:
        if not number % i:
            break
        i += 1
    else:
        print(number)
    number += 1
