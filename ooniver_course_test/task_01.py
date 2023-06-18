number = int(input('Enter your number: '))

for i in range(number // 2 + 1):
    if i > 0:
        if number % i == 0:
            print(i)
