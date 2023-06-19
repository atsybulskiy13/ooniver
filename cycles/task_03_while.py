number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1 > number2:
    i = number2
    while i < number1:
        if i % 5 != 0:
            if i == 23 or i == 32:
                break
            print(i)
        i += 1
