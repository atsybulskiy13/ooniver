def if_palindrom():

    splited_string = (input('Enter your string: ')).split()

    join_string = ''.join(splited_string)

    new_string = ''

    for char in join_string:
        new_string = char + new_string

    if new_string == join_string:
        print("It's palindrom!")
    else:
        print("It's not palindrom!")


if_palindrom()
