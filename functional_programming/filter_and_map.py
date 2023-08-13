class User:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return f'{self.name}, {self.age}, {self.sex}, {self.salary if hasattr(self, "salary") else ""}'


user1 = User('Sasha', 22, 'male')
user2 = User('Denero', 23, 'male')
user3 = User('Anya', 25, 'female')
user4 = User('Mish', 30, 'female')
user5 = User('Tom', 14, 'male')

users = [user1, user2, user3, user4, user5]

users_with_new_age_list = list(
    filter(lambda user: user.age + 1 if 'a' in user.name or 'e' in user.name else None, users)
)
print(users_with_new_age_list)


users_with_salary = list(map(lambda user: setattr(user, 'salary', 100), users))

# users_with_salary = list(map(lambda user: setattr(user, 'salary', 1000), filter(lambda user: user.age > 18, users)))
for user in users:
    print(user)
