def quadratic_equation(a: int, b: int = 0, c: int = 0):

    x_1 = x_2 = None

    if a != 0:

        d = (b ** 2) - (4 * a * c)

        if d < 0:
            print('No roots!')
        elif d == 0:
            x_1 = x_2 = -b / (2 * a)
        else:
            x_1 = (-b + (d ** 0.5)) / (2 * a)
            x_2 = (-b - (d ** 0.5)) / (2 * a)

        return x_1, x_2

    else:
        print("It's not a quadratic equation, a cannot be = 0")
        return x_1, x_2


x1, x2 = quadratic_equation(5, 3, -26)
print(x1, x2)
