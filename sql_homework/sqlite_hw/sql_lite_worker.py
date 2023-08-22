from sqlite3 import connect

connection = connect('school.db')

cursor = connection.cursor()

cursor.executescript('''
    CREATE TABLE persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname VARCHAR,
    lastname VARCHAR,
    sex VARCHAR,
    age INTEGER
    );

    CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER,
    course INTEGER,
    FOREIGN KEY (person_id) REFERENCES persons(id)
    );

    CREATE TABLE marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    math INTEGER,
    literature INTEGER,
    chemistry INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id)
    )
''')

persons = [
    ('Sasha', 'Tsybulskiy', 'male', 22),
    ('Denis', 'Cvach', 'male', 22),
    ('Anya', 'Dmitrieva', 'female', 25)
]

students_courses = [
    (1, 2),
    (2, 1),
    (3, 5)
]

students_marks = [
    (1, 9, 7, 8),
    (2, 8, 7, 9),
    (3, 7, 8, 9)
]


cursor.executemany('INSERT INTO persons VALUES (NULL, ?, ?, ?, ?)', persons)

cursor.executemany('INSERT INTO students (person_id, course) VALUES (?, ?)', students_courses)

cursor.executemany('INSERT INTO marks VALUES (NULL, ?, ?, ?, ?)', students_marks)

connection.commit()

cursor.execute(
    'SELECT * FROM persons JOIN students on persons.id = students.person_id'
)

result = cursor.fetchall()
print(result)

cursor.execute('''
    SELECT math FROM marks m JOIN persons p on m.student_id = p.id
    WHERE p.firstname = "Sasha"
''')

result = cursor.fetchall()
print(result)
