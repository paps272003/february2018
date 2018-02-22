
class View:

	def takeInput(self, prompt):
		return input( prompt )

	def printOutput(self, output):
		print(output)

	def printAccount(self, account):
		print("Account type:", account[2])
		print("Account Balance:",account[1])

	def mainMenu(self):
		print("1. Create account")
		print("2. Log in")
		print("3. Exit")

		return input("Enter a number")

	def acctChoiceMenu(self):
		print("1. Create new account")
		print("2. Access accout")
		print("3. Log Out")

		return input("Enter a number")

	def accountChoice(self, account_list):
		index = 1

		for account in account_list:
			print(index,". ",account[2])
			index = index + 1


		return input("Enter a number: ")


	def accountMenu(self):
		print("1. Deposit")
		print("2. Withdraw")
		print("3. View Account")
		print("4. Transfer Funds")
		print("5. Log out")

		return input("Enter a number")