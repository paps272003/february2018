import sqlite3

class Model:
	def __init__(self):
		self.connection = sqlite3.connect("bank.db")

		self.cursor = self.connection.cursor()

	def insertUser(self, username, password, name):
		self.cursor.execute("INSERT INTO users(username,password,name) VALUES (?,?,?)", (username, password, name))

		self.connection.commit()

	def insertAccount(self, acct_type, balance, user_id):
		self.cursor.execute("INSERT INTO accounts(balance,acct_type,user_id) VALUES (?,?,?)", (balance, acct_type, user_id) )

		self.connection.commit()

	def login(self, username, password):
		self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password) )

		return self.cursor.fetchone()

	def updateBalance(self, acct_id, new_balance):
		self.cursor.execute("UPDATE accounts SET balance=? WHERE id=?", (new_balance, acct_id) )

		self.connection.commit()

	def selelctAcctById(self, acct_id):
		self.cursor.execute("SELECT * FROM accounts WHERE id=?", (acct_id,) )

		return self.cursor.fetchone()

	def selectAcctsByUser(self, user_id):
		self.cursor.execute("SELECT * FROM accounts WHERE user_id=?", (user_id,) )

		return self.cursor.fetchall()

	def checkUsername(self, username):
		self.cursor.execute("SELECT * FROM users WHERE username=?", (username,) )

		return self.cursor.fetchone()


if __name__ == "__main__":
	my_model = Model()

	my_model.cursor.execute('''CREATE TABLE users(
											id INTEGER PRIMARY KEY,
											username VARCHAR(30),
											password VARCHAR(50),
											name VARCHAR(30)) ''')

	my_model.cursor.execute('''CREATE TABLE accounts(
											id INTEGER PRIMARY KEY,
											balance REAL,
											acct_type VARCHAR(30),
											user_id INTEGER,
											FOREIGN KEY(user_id) REFERENCES users(id) )''')

	my_model.connection.commit()

	my_model.connection.close()