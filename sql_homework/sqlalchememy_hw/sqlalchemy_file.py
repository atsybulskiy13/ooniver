from sqlalchemy import create_engine, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

engine = create_engine("sqlite:///school2.db", echo=True)


class Base(DeclarativeBase):
    pass


class Person(Base):
    __tablename__ = 'persons'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    firstname: Mapped[str] = mapped_column(String())
    lastname: Mapped[str] = mapped_column(String())
    sex: Mapped[str] = mapped_column(String())
    age: Mapped[int] = mapped_column(Integer())
    student: Mapped['Student'] = relationship('Student', back_populates='person')

    def __init__(self, firstname, lastname, sex, age):
        self.firstname = firstname
        self.lastname = lastname
        self.sex = sex
        self.age = age


class Student(Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    person_id: Mapped[int] = mapped_column(ForeignKey("persons.id"))
    course: Mapped[int] = mapped_column(Integer())
    person: Mapped['Person'] = relationship('Person', back_populates='student')
    marks: Mapped['Marks'] = relationship('Marks', back_populates='student')

    def __init__(self, person, course):
        self.person = person
        self.course = course


class Marks(Base):
    __tablename__ = 'marks'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(ForeignKey('students.id'))
    math: Mapped[int] = mapped_column(Integer())
    literature: Mapped[int] = mapped_column(Integer())
    chemistry: Mapped[int] = mapped_column(Integer())
    student: Mapped['Student'] = relationship('Student', back_populates='marks')

    def __init__(self, student, math, literature, chemistry):
        self.student = student
        self.math = math
        self.literature = literature
        self.chemistry = chemistry


Base.metadata.create_all(engine)
