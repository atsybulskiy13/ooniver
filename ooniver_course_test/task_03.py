number = int(input('Enter your number: '))

factorial = 1

if number == 0:
    print(f'Factorial {number} = {factorial}')
elif number < 0:
    print('There is no factorial for number < 0')
else:
    for i in range(number + 1):
        if i > 0:
            factorial *= i
    print(f'Factorial {number} = {factorial}')
