def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def super_factorial(n: int) -> int:
    if not isinstance(n, int):
        raise Exception('this must be an integer number')
    if n < 0:
        raise Exception('the number must be more than 0')
    return factorial(n)
