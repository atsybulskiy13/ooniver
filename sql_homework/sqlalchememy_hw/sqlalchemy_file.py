from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey

engine = create_engine("sqlite:///school2.db", echo=True)


class Base(DeclarativeBase):
    pass


class SchoolPerson(Base):
    __tablename__ = 'persons'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    firstname: Mapped[str] = mapped_column()
    lastname: Mapped[str] = mapped_column()
    sex: Mapped[str] = mapped_column()
    age: Mapped[int]

    def __init__(self, firstname, lastname, sex, age):
        self.firstname = firstname
        self.lastname = lastname
        self.sex = sex
        self.age = age


class SchoolStudent(Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    person_id: Mapped[int] = mapped_column(ForeignKey("persons.id"))
    course: Mapped[int] = mapped_column()

    def __init__(self, person_id, course):
        self.person_id = person_id
        self.course = course


class StudentMarks(Base):
    __tablename__ = 'marks'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(ForeignKey('students.id'))
    math: Mapped[int] = mapped_column()
    literature: Mapped[int] = mapped_column()
    chemistry: Mapped[int] = mapped_column()

    def __init__(self, student_id, math, literature, chemistry):
        self.student_id = student_id
        self.math = math
        self.literature = literature
        self.chemistry = chemistry


Base.metadata.create_all(engine)
