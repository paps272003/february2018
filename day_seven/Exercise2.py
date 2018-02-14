import sqlite3
import csv

def createTables():

	connection = sqlite3.connect("employees.db")

	cursor = connection.cursor()

	cursor.execute('''CREATE TABLE employees(
										id INTEGER PRIMARY KEY,
										name VARCHAR(50),
										country VARCHAR(50),
										email VARCHAR(100) )''')

	cursor.execute('''CREATE TABLE phonenumbers(
										id INTEGER PRIMARY KEY,
										phonenumber VARCHAR(20),
										employee_id INTEGER,
										FOREIGN KEY (employee_id) REFERENCES employees(id) ) ''')

	connection.commit()

	connection.close()

# createTables()

connection = sqlite3.connect("employees.db")

cursor = connection.cursor()


with open("employees.csv") as csvfile:
	lines = csv.reader( csvfile )

	for line in lines:
		print(line)

		cursor.execute("INSERT INTO employees(name, country, email) VALUES (?,?,?)", ( line[0], line[5], line[4] ) )

		lastrow = cursor.lastrowid

		cursor.execute("INSERT INTO phonenumbers(phonenumber, employee_id) VALUES (?,?)", (line[1], lastrow))

		cursor.execute("INSERT INTO phonenumbers(phonenumber, employee_id) VALUES (?,?)", (line[2], lastrow))

		cursor.execute("INSERT INTO phonenumbers(phonenumber, employee_id) VALUES (?,?)", (line[3], lastrow))		

		connection.commit()

	connection.close()