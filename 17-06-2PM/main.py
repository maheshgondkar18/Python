import pymongo

client=pymongo.MongoClient()

mydb=client["mydb"]

mycol=mydb["Employee"]

data={'Name':'Sai', 'Age':'23'}
mycol.insert_one(data)

datalist=[{'Name':'Mahesh','Age':'23'},{'Name':'Sahil','Age':'22'}]
x = mycol.insert_many(datalist)

for x in mycol.find():
    print(x)