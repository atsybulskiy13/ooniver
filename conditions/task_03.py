age = int(input("Enter your age: "))

if age <= 18:
    print("You are too young to work with this program!")
elif age >= 65:
    print("You are too old to work with this program!")
else:
    print("Your age is", age)
    print("You can proceed to work, man!")
