student1 = {}
student2 = {}
student3 = {}

students = [student1, student2, student3]

for index in range(len(students)):
    students[index]['name'] = input(f'Enter name for student {index + 1}: ')
    students[index]['last_name'] = input(f'Enter last name for student {index + 1}: ')
    students[index]['age'] = int(input(f'Enter age for student {index + 1}: '))
    students[index]['form'] = int(input(f'Enter form for student {index + 1}: '))
    students[index]['math_score'] = int(input(f'Enter math score for student {index + 1}: '))
    students[index]['eng_score'] = int(input(f'Enter english score for student {index + 1}: '))
    students[index]['sport_score'] = int(input(f'Enter sport score for student {index + 1}: '))

print(f'Original students dict:\n {students}')
print()

for index in range(len(students)):
    students[index]['avg_score'] = (students[index]['math_score'] + students[index]['eng_score'] + students[index]['sport_score']) / 3

print(f'Students dict with avg score:\n {students}')
