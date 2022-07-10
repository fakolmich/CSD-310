from pymongo import MongoClient
url= "mongodb+srv://admin:admin123@cluster0.dwrx5.mongodb.net/?retryWrites=true&w=majority"
client  = MongoClient(url)
db = client.pytech
docs= db.students.find({})
print('-- DISPLAYING STUDENTS DOCUMENTS from find() QUERY --- ')
for doc in docs : print(doc)

doc = db.students.find_one({"student_id":"1007"})
print('-- DISPLAYING STUDENT DOCUMENTS from find_one() QUERY --- ')
print(doc)