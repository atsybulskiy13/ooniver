import datetime
# from bson import ObjectId

from pymongo import MongoClient

client = MongoClient()

db = client.super_test_database

posts = db.posts

post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": [
        "mongodb", "python", "pymongo"
    ],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}
# post_1 = posts.insert_one(post)
# print(post_1)
#
# posts = posts.find()
#
# print(db.list_collection_names())

post_1_id = posts.insert_one(post).inserted_id

document = posts.find_one({"_id": post_1_id})
