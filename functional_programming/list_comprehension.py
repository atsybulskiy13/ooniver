# from random import randint

# my_list = [1, 2, 3, 5, 6, 7, 8, 9, 0]
#
# new_list = [number + 1 for number in my_list]
# print(new_list)
#
#
# class User:
#
#     def __init__(self, age):
#         self.age = age
#
#
# user1 = User(12)
# user2 = User(22)
# user3 = User(35)
#
# users = [user1, user2, user3]
#
# age_list = [user.age + 1 for user in users]
# print(age_list)
#
# new_list2 = [number for number in my_list if number % 2 == 0]
# print(new_list2)
#
# new_age_list = [user.age for user in users if user.age > 18]
# print(new_age_list)
a = 1
b = 10
matrix = [[number for number in range(b * number - 10 + 1, b * number + 1)] for number in range(1, 11)]

for row in matrix:
    print(row)
