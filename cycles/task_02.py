my_list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list2 = []

for i in my_list1:
    if i % 2 == 0:
        my_list2.append(i)
        my_list2.append(i)

    else:
        i = i ** i
        my_list2.append(i)

print(my_list2)
