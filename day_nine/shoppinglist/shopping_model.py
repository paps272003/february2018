import sqlite3

class Model:

	def __init__(self):
		self.connection = sqlite3.connect("list.db")

		self.cursor = self.connection.cursor()

	def insertItem(self, name):
		self.cursor.execute("INSERT INTO shoppinglist(name,checked) VALUES (?,?)", (name, "UNCHECKED") )

		self.connection.commit()

	def selectAllItems(self):
		self.cursor.execute("SELECT * FROM shoppinglist")

		return self.cursor.fetchall()

	def checkId(self, item_id):
		self.cursor.execute("SELECT id FROM shoppinglist WHERE id=?", (item_id,) )

		return self.cursor.fetchone()

	def updateChecked(self, item_id, checked):
		self.cursor.execute("UPDATE shoppinglist SET checked=? WHERE id=?", (checked, item_id) )

		self.connection.commit()

	def closeConnection(self):

		self.connection.close()

if __name__ == "__main__":
	my_model = Model()

	my_model.cursor.execute(''' CREATE TABLE shoppinglist(
														id INTEGER PRIMARY KEY,
														name VARCHAR(30),
														checked VARCHAR(9)) ''')

	my_model.connection.commit()

	my_model.closeConnection()