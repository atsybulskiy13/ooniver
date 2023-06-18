with open('poems.txt') as my_file:
    data = my_file.read()

with open('poems2.txt', 'w') as my_file:
    my_file.write(data)
