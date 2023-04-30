import pymongo
my_client = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = my_client['my_database']
print(mydb)
