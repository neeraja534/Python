import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
print(myclient.list_database_names())
mydb=myclient["cmrec"]
'''mydblist=myclient.list_database_names()
if "cmrec" in mydblist:
    print("database is exist")
else:
    print("database doesn't exist")
'''
mycol=mydb["csea"]
mylist=mydb.list_collection_names()
if "csea" in mylist:
    print("is exists")
else:
    print("Doesn't exists")