from sqlalchemy.orm import sessionmaker

from sqlalchemy_file import engine, Person, Student, Marks

Session = sessionmaker(bind=engine)
session = Session()

person_1 = Person('Alex', 'Tsybulskiy', 'male', 22)
person_2 = Person('Deniska', 'Cvach', 'male', 23)
person_3 = Person('Anya', 'Dmitrieva', 'female', 25)

persons = [person_1, person_2, person_3]

student_1 = Student(person_1, 3)
student_2 = Student(person_2, 4)
student_3 = Student(person_3, 5)

students = [student_1, student_2, student_3]

student_1_marks = Marks(student_1, 8, 6, 7)
student_2_marks = Marks(student_2, 7, 8, 9)
student_3_marks = Marks(student_3, 6, 7, 10)

student_marks = [student_1_marks, student_2_marks, student_3_marks]
session.add_all([*persons, *students, *student_marks])
session.commit()
