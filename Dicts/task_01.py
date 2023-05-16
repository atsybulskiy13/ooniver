user1 = {
    'name': 'Sasha',
    'last_name': 'Tsyb',
    'age': 22
}
user2 = {
    'name': 'Denero',
    'last_name': 'Cvash',
    'age': 49
}
user3 = {
    'name': 'Anya',
    'last_name': 'Dmitr',
    'age': 150,
    'hobby': 'asdsadad'
}

users = [user1, user2, user3]

key = 'hobby'

hobbies = ['sportsmen', 'komsomol', 'krasavec']

for index in range(len(users)):
    users[index]['age'] += 1
    if not key in users[index]:
        users[index][key] = hobbies[index]

print(users)

print()

users.remove(user1)
print(users)

for index in range(len(users)):
    del users[index]['hobby']

print(users)
