#STEP 1: Import sqlite3
import sqlite3

#STEP 2: Connect to database and store connection in variable
connection = sqlite3.connect("cars.db")

#Step 3: open a cursor object and store in varaible
cursor = connection.cursor()

#STEP 4: execute commands
# cursor.execute('''CREATE TABLE cars(
# 						id INTEGER PRIMARY KEY,
# 						make VARCHAR(50),
# 						model VARCHAR(50),
# 						year INTEGER)''')

#STEP 5: Run the command
connection.commit()

model = input("Enter the model: ")

cursor.execute("INSERT INTO cars(make,model,year) VALUES (?,?,?)", ("Toyota",model, 2009) )

connection.commit()

cursor.execute("SELECT * FROM cars")

cars = cursor.fetchall()

print(cars)

#LAST STEP: close connection to database
connection.close()