from pymongo import MongoClient
from bson import ObjectId

client = MongoClient()

books_db = client.books_database

books = books_db.books

paper_book = {
    'type': 'paper',
    'name': 'treasure Island',
    'author': 'Gena',
    'page_amount': 300,
    'edition': 3,
    'is_deleted': False
}

e_book = {
    'type': 'electronic',
    'name': 'Oppenheimer',
    'author': 'Vasya',
    'size_mb': 30,
    'is_deleted': False
}

audio_book = {
    'type': 'audio',
    'name': 'green Mile',
    'author': 'Petya',
    'duration_min': 120,
    'is_deleted:': False
}


books = books.insert_many([paper_book, e_book, audio_book])


def get_all_books():
    books_collection = books.find()
    books_list = [book for book in books_collection]
    return books_list


def get_book_by_id(book_id):
    book = books.find_one({'_id': ObjectId(book_id)})
    return book


def delete_book_by_id(book_id):
    books_db.books.update_one({'_id': ObjectId(book_id)}, {'$set': {'is_deleted': True}})


def get_books_by_author(author):
    book_collection = books.find({'author': author})
    book_list = [book for book in book_collection]

    return book_list


book_id = '64ce6f4e3635c8559114089c'

book = get_book_by_id(book_id)
print(book)

books_by_author = get_books_by_author('Gena')
print(books_by_author)

delete_book_by_id(book_id)

all_books = get_all_books()
print(all_books)
