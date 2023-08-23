from filter_and_map_hw import User


user1 = User('Sasha', 22, 'male')
user2 = User('Denero', 23, 'male')
user3 = User('Anya', 25, 'female')
user4 = User('Mish', 30, 'female')
user5 = User('Tom', 14, 'male')

users = [user1, user2, user3, user4, user5]

users_with_new_age_list = [setattr(user, 'age', user.age + 1) for user in users if 'a' in user.name or 'e' in user.name]
for user in users:
    print(user)

users_with_salary_list = [setattr(user, 'salary', 300) for user in users if user.age > 18]
for user in users:
    print(user)

string_name_age_list = [f'{user.name}: {user.age}' for user in users]
print(string_name_age_list)
