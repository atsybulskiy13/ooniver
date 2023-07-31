# from functools import reduce

# print((lambda a, b, c: a + b + c)(2, 3, 4))
#
# result = (lambda a, b, c: a * b * c)(1, 2, 3)
#
# print(result)
#
# print(f'Perimeter = {(lambda a, b: (a + b) * 2)(2, 4)}')
#
# lst = [1, 2, 3, 4, 5]
# square = list(map(lambda x: x ** 2, lst))
# print(square)
#
#
# new_list = [1, 2, 3, 4, 5]
# numbers = list(map(lambda a: str(a), new_list))
# print(numbers)
#
#
# word_list = ['car', 'house', 'author']
# new_word_list = list(map(lambda word: word + str(len(word)), word_list))
# print(new_word_list)
#
#
# lst = [1, 2, 3, 4, 5]
# even = list(filter(lambda x: x % 2 == 0, lst))
# print(even)

#
# word_list = ['car', 'house', 'author']
# new_word_list = list(filter(lambda word: not len(word) % 2, word_list))
# print(new_word_list)
#
# new_word_list = list(filter(lambda word: 'a' in word, word_list))
# print(new_word_list)
# #
# # a = 100
# # x = a - 1
# result = reduce(lambda a, x: a + x, range(0, 101))
# print(result)
#
# char_list = ['f', 'a', 't', 'h', 'e', 'r']
# word = reduce(lambda a, b: a + b, char_list)
# print(word)
