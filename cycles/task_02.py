my_list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in my_list1:
    if i % 2 == 0:
        print(i, end="")
        print(i, end=" ")

    else:
        print(i ** i, end=" ")
