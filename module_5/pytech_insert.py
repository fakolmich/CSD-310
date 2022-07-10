from pymongo import MongoClient
url= "mongodb+srv://admin:admin123@cluster0.dwrx5.mongodb.net/?retryWrites=true&w=majority"
client  = MongoClient(url)
students = client.pytech.students
kolawole = {
    "student_id":"1007",
    "first_name": "Kolawole",
    "last_name" : "Matthew"
}
charles = {
     "student_id":"1008",
     "first_name": "Charles",
     "last_name" : "Law"
}
katrine = {
     "student_id":"1009",
     "first_name": "Katrine",
     "last_name" : "Price"
}
kolawole_student_id = students.insert_one(kolawole).inserted_id
charles_student_id = students.insert_one(charles).inserted_id
katrine_student_id = students.insert_one(katrine).inserted_id
print('Inserted student record Kolawole into student collection with document id '+ str(kolawole_student_id))
print('Inserted student record Charles into student collection with document id '+ str(charles_student_id))
print('Inserted student record Katrine into student collection with document id '+ str(katrine_student_id))