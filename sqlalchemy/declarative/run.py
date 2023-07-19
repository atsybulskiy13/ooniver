from sqlalchemy.orm import sessionmaker

from declarative_approach import engine, LibraryPerson, Book

Session = sessionmaker(bind=engine)
session = Session()
user_1 = LibraryPerson('Alex', 'Tsybulskiy')
user_2 = LibraryPerson('Deniska', 'Cvach')
user_3 = LibraryPerson('Anya', 'Dmitrieva')
book_1 = Book("Deniska's stories", 'Tom Kruz', user_1)
session.add_all([user_1, user_2, user_3, book_1])
session.commit()
