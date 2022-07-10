from pymongo import MongoClient
url= "mongodb+srv://admin:admin123@cluster0.dwrx5.mongodb.net/?retryWrites=true&w=majority"
client  = MongoClient(url)
db = client.pytech
docs= db.students.find({})
print('-- DISPLAYING STUDENTS DOCUMENTS from find() QUERY --- ')
for doc in docs : print(doc)
new_record = {
     "student_id":"10010",
     "first_name": "Jack",
     "last_name" : "Bower"
}
new_student_id = db.students.insert_one(new_record).inserted_id
print('-- INSERT STATEMENTS --')
print('Inserted student record into student collection with document id '+ str(new_student_id))
doc = db.students.find_one({"student_id":"10010"})
print('-- DISPLAYING STUDENTS TEST DOC --')
print(doc)
result = db.students.delete_one({"student_id":"10010"})

docs= db.students.find({})
print('-- DISPLAYING STUDENTS DOCUMENTS from find() QUERY --- ')
for doc in docs : print(doc)
