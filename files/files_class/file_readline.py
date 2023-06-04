my_file = open('poems.txt')

while line := my_file.readline():
    print(line)

my_file.close()
