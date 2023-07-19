from sqlite3 import connect
# создаем подключение
connection = connect('fruits.db')
# создаем курсор
cursor = connection.cursor()

# cursor.executescript('''
# CREATE TABLE fruit (
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR
# );
# CREATE TABLE basket (
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     fruit_id INTEGER,
#     quantity INTEGER,
#     FOREIGN KEY (fruit_id) REFERENCES  fruit(id)
# )
# ''')

# cursor.execute('''
# INSERT INTO fruit (name) VALUES (?)
# ''', ('banana',))
# cursor.execute('''
# INSERT INTO fruit (name) VALUES (?)
# ''', ('apple',))

# fruits = [(10, 'orange'),(11, 'pineapple'),(12, 'peach'),(13, 'watermelon')]
# cursor.executemany('INSERT INTO fruit (id, name) VALUES (?, ?)', fruits)
#
# connection.commit()

cursor.execute(
    'SELECT name FROM fruit'
)

result = cursor.fetchall()
print(result)
