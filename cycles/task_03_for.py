number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1 > number2:
    for i in range(number2, number1):
        if i % 5 != 0:
            if i == 23 or i == 32:
                break
            print(i)
