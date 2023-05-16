student1 = {}
student2 = {}
student3 = {}

students = [student1, student2, student3]

for student in range(len(students)):
    students[student]['name'] = input(f'Enter name for student {student + 1}: ')
    students[student]['last_name'] = input(f'Enter last name for student {student + 1}: ')
    students[student]['age'] = int(input(f'Enter age for student {student + 1}: '))
    students[student]['form'] = int(input(f'Enter form for student {student + 1}: '))
    students[student]['math_score'] = int(input(f'Enter math score for student {student + 1}: '))
    students[student]['eng_score'] = int(input(f'Enter english score for student {student + 1}: '))
    students[student]['sport_score'] = int(input(f'Enter sport score for student {student + 1}: '))

print(f'Original students dict:\n {students}')
print()

for index in range(len(students)):
    students[index]['avg_score'] = (students[index]['math_score'] + students[index]['eng_score'] + students[index]['sport_score']) / 3

print(f'Students dict with avg score:\n {students}')
