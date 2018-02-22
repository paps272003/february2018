from bank_model import Model
from bank_view import View

def accessAccount(user, account_info, my_model, my_view):
	running_my_account = True
	while running_my_account == True:

		choice = my_view.accountMenu()

		if choice == "1":
			#Deposit

			deposit_amount = my_view.takeInput("HOw much to deposit: ")

			try:
				deposit_amount = float( deposit_amount )

				new_balance = account_info[1] + deposit_amount

				my_model.updateBalance(account_info[0], new_balance)

				account_info[1] = new_balance
			except:
				my_view.printOutput("Invalid number, try again")

		elif choice == "2":
			#Withdraw

			withdraw_amount = my_view.takeInput("How much to withdraw: ")

			try:
				withdraw_amount = float(withdraw_amount)

				if withdraw_amount > 0 and withdraw_amount <= account_info[1]:
					new_balance = account_info[1] - withdraw_amount

					my_model.updateBalance(account_info[0], new_balance)

					account_info[1] = new_balance
				else:
					my_view.printOutput("INvalid funds. try again")

			except:
				my_view.printOutput("Invalid number, try again")

		elif choice == "3":

			account_info = my_model.selectAcctById(account_info[0])

			my_view.printAccount(account_info)

		elif choice == "4":
			pass
		elif choice == "5":
			running_my_account = False
		else:
			my_view.printOutput("Invalid choice, try again")

def accountMenu(user, my_model, my_view):
	running_accounts = True

	while running_accounts == True:
		choice = my_view.acctChoiceMenu()

		if choice == "1":
			acct_type = my_view.takeInput("Enter your account type: ")

			my_model.insertAccount(acct_type, 100.0, user[0] )

		elif choice == "2":

			all_accts = my_model.selectAcctsByUser(user[0])

			if len(all_accts) == 0:
				my_view.printOutput("No accounts. Please create an account first")
			elif len(all_accts) == 1:
				accessAccount(user, all_accts[0], my_model, my_view)
			else:
				account_choice = my_view.accountChoice(all_accts)

				try:
					account_choice = int( account_choice ) - 1

					# print(account_choice)

					# print(all_accts[account_choice])

					# print(len(all_accts))

					# print(0 <= account_choice)

					# print(account_choice < len(all_accts))

					if 0 <= account_choice and account_choice < len(all_accts):
						accessAccount(user, all_accts[account_choice], my_model, my_view)
					else:
						my_view.printOutput("Invalid entry try again")

				except ValueError:
					my_view.printOutput("Invalid Entry, try again.")

		elif choice == "3":
			running_accounts = False
		else:
			my_view.printOutput("Invalid entery, try again")





my_model = Model()
my_view = View()

running = True

while running == True:
	choice = my_view.mainMenu()

	if choice == "1":
		username = my_view.takeInput("Enter a username: ")
		password = my_view.takeInput("Enter a password: ")
		name = my_view.takeInput("Enter your name: ")

		exists = my_model.checkUsername(username)

		if exists == None:
			my_model.insertUser(username, password, name)
		else:
			my_view.printOutput("Username already taken. Choose another username")

	elif choice == "2":

		username = my_view.takeInput("Enter your username: ")
		password = my_view.takeInput("Enter your password: ")

		valid = my_model.login(username, password)

		if valid == None:
			my_view.printOutput("Not a valid username/password. Try again")
		else:
			accountMenu(valid, my_model, my_view)

	elif choice == "3":
		running = False
	else:
		m_view.printOutput("Not a valid choice, try again")