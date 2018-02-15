import sqlite3

class Model:

	def __init__(self, database_name):
		self.connection = sqlite3.connect(database_name)

		self.cursor = self.connection.cursor()

	def selectAllPeople(self):
		self.cursor.execute("SELECT * FROM people")

		return self.cursor.fetchall()

	def selectOnePerson(self, person_id):
		self.cursor.execute("SELECT * FROM people WHERE id=?", (person_id,) )

		return self.cursor.fetchone()

	def insertPerson(self, name, address, ssn):
		self.cursor.execute("INSERT INTO people(name,address,ssn) VALUES (?,?,?)", (name, address, ssn) )

		self.connection.commit()

	def closeConnection(self):
		self.connection.close()


if __name__ == "__main__":
	my_model = Model("employees.db")

	my_model.cursor.execute('''CREATE TABLE people(
												id INTEGER PRIMARY KEY,
												name VARCHAR(30),
												address VARCHAR(100),
												ssn VARCHAR(12)) ''')

	my_model.connection.commit()

	my_model.closeConnection()