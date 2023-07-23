from sqlalchemy.orm import sessionmaker

from sqlalchemy_file import engine, SchoolPerson, SchoolStudent, StudentMarks

Session = sessionmaker(bind=engine)
session = Session()

person_1 = SchoolPerson('Alex', 'Tsybulskiy', 'male', 22)
person_2 = SchoolPerson('Deniska', 'Cvach', 'male', 23)
person_3 = SchoolPerson('Anya', 'Dmitrieva', 'female', 25)

student_1 = SchoolStudent(1, 3)
student_2 = SchoolStudent(2, 4)
student_3 = SchoolStudent(3, 5)

student_1_marks = StudentMarks(1, 8, 6, 7)
student_2_marks = StudentMarks(2, 7, 8, 9)
student_3_marks = StudentMarks(3, 6, 7, 10)

persons = [person_1, person_2, person_3]

students = [student_1, student_2, student_3]

student_marks = [student_1_marks, student_2_marks, student_3_marks]

session.add_all([*persons, *students, *student_marks])
session.commit()
