from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import List

engine = create_engine("sqlite:///library2.db", echo=True)


class Base(DeclarativeBase):
    pass


class LibraryPerson(Base):
    __tablename__ = 'person'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    firstname: Mapped[str] = mapped_column(String(30))
    lastname: Mapped[str] = mapped_column(String(40))
    create_date: Mapped[datetime] = mapped_column(insert_default=datetime.now())
    book: Mapped[List["Book"]] = relationship(back_populates="person")

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class Book(Base):
    __tablename__ = 'book'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100))
    author: Mapped[str] = mapped_column(String(30))
    person_id: Mapped[int] = mapped_column(ForeignKey("person.id"))
    person: Mapped['LibraryPerson'] = relationship(back_populates="book")

    def __init__(self, title, author, person=None):
        self.title = title
        self.author = author
        self.person = person


Base.metadata.create_all(engine)
