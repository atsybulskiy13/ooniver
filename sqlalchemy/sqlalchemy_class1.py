from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///library1.db', echo=True)
with engine.connect() as connection:
    # create_table_query = '''
    #     CREATE TABLE book (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         title VARCHAR,
    #         pages INTEGER,
    #         author VARCHAR,
    #         price FLOAT,
    #         release_year INTEGER
    #     );
    # '''
    # query = text(create_table_query)
    # connection.execute(query)
    insert_book_into_table = '''
    INSERT INTO book (title, pages, author, price, release_year)
    VALUES (:title, :pages, :author, :price, :release_year)
    '''

    query = text(insert_book_into_table).bindparams(
        title='DeniskinyR',
        pages=200,
        author='Victor Dragunskiy',
        price=10,
        release_year=1977,
    )
    connection.execute(query)

    if input('Yy - > ') in 'Yy':
        connection.commit()
    else:
        connection.rollback()
