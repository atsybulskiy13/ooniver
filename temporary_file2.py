name = input("Enter your name: ")
second_name = input("Enter your secondname: ")
work_place = input("Enter your work place: ")
age = int(input("Enter your work age: "))

print(work_place, "\n", "----------", "\n", second_name, " ", name, ", ", age, sep="")

user1 = {
    "name": "Sasha",
    "second_name": "Tsybulskiy",
    "work_place": "Softvoya",
    "age": 44
}

user2 = {
    "name": name,
    "second_name": second_name,
    "work_space": work_place,
    "age": age
}

users = [user1, user2]

avg_age = int((user1["age"] + user2["age"]) / users.__len__())

print("The average age is: ", avg_age)
