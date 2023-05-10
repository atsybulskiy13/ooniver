for number in range(0, 1001):
    sum1 = 0
    for i in str(number):
        sum1 += int(i)
    if sum1 > 1:
        for z in range(2, sum1):
            if sum1 % z == 0:
                break
        else:
            print(number, " - > ", sum1)
