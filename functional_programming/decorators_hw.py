def second_elem_to_string_decorator(func):
    def wrapper(x):
        result = func(x)

        new_list = [str(result[i]) if i % 2 else result[i] for i in range(len(result))]
        return new_list

    return wrapper


@second_elem_to_string_decorator
def second_elem_to_string(number_list):
    return number_list


number_list = [x for x in range(10)]
print(number_list)


new_list = second_elem_to_string(number_list)
print(new_list)


def list_reverse_decorator(func):
    def wrapper(*args):
        args = func(*args)
        new_args = []
        for i in args:
            new_args.insert(0, i)

        return tuple(new_args)

    return wrapper


@list_reverse_decorator
def args_function(*args):
    return args


a = 1
b = 3
c = 5

args = args_function(a, b, c)
print(args)
