from sqlalchemy.orm import sessionmaker

from sqlalchemy_file import engine, Person, Student, Marks

Session = sessionmaker(bind=engine)
session = Session()

person_1 = Person('Alex', 'Tsybulskiy', 'male', 22)
person_2 = Person('Deniska', 'Cvach', 'male', 23)
person_3 = Person('Anya', 'Dmitrieva', 'female', 25)

persons = [person_1, person_2, person_3]
session.add_all([*persons])
session.commit()

student_1 = Student(person_1.id, 3)
student_2 = Student(person_2.id, 4)
student_3 = Student(person_3.id, 5)

students = [student_1, student_2, student_3]
session.add_all([*students])
session.commit()

student_1_marks = Marks(student_1.id, 8, 6, 7)
student_2_marks = Marks(student_2.id, 7, 8, 9)
student_3_marks = Marks(student_3.id, 6, 7, 10)

student_marks = [student_1_marks, student_2_marks, student_3_marks]
session.add_all([*student_marks])
session.commit()
