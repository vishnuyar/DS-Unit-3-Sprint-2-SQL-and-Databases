import pymongo


client = pymongo.MongoClient("mongodb+srv://mongoadmin:2BlYV2t3X4jws3XR@cluster0-uosnx.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
