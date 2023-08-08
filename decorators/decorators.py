from datetime import datetime


def decorator_ot_sashki(func):
    def wrapper():
        print('Действия до')
        time_before = datetime.now()
        # действия до
        func()
        # действия после
        print('Действия после')
        time_after = datetime.now()

        print(f'function time - {time_after - time_before} sec')

    return wrapper


@decorator_ot_sashki
def say_hello():
    print('Zdarova epta!')


say_hello()
