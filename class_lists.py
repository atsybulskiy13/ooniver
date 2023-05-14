words1 = [4, 6, 8]

words_len = len(words1)

for number in range(words_len):
    words1[number] += 1

print(words1)

words2 = [4, 6, 8]

number = 0

while number < words_len:
    words2[number] += 1
    number += 1

print(words2)

if words1 == words2:
    print('Списки равны')
else:
    print('Списки не равны')

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = list1[2:10:3]

print(list1[3:])
print(list1[:7])
print(list1[:])
print(list1[8:3:-2])
print(list2)

list_a = [1, 2, 3]

list_b = []

for i in list_a:
    list_b.insert(0, i)

print(list_b)

str1 = 'Александр Сергеевич Пушкин'

str2 = str1[1::2]
print(str2)

lst = str1.split('а')
print(lst)
