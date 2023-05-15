for number in range(2, 101):
    for i in range(2, number):
        if not number % i:
            break
    else:
        print(number)
