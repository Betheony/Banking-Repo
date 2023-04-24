import mysql.connector

connection = mysql.connector.connect(
    user= 'root', 
    database= 'example', 
    password= 'x770948Boolaid!'
    )

cursor = connection.cursor()

addData = ('INSERT INTO students (name, age, grade) VALUES ("lala", 7, 11)')

cursor.execute(addData)

testQuery = ("SELECT * FROM students")
cursor.execute(testQuery)

for item in cursor:
    print(item)

connection.commit()
cursor.close()
connection.close()