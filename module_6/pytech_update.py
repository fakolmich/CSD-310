from pymongo import MongoClient
url= "mongodb+srv://admin:admin123@cluster0.dwrx5.mongodb.net/?retryWrites=true&w=majority"
client  = MongoClient(url)
db = client.pytech
result = db.students.update_one({"student_id":"1007"},{"$set":{"last_name":"Matthew 001"}})

docs= db.students.find({})
print('-- DISPLAYING STUDENTS DOCUMENTS from find() QUERY --- ')
for doc in docs : print(doc)
print('-- DISPLAYING STUDENT DOCUMENTS 1007 ')
doc = db.students.find_one({"student_id":"1007"})
print(doc)