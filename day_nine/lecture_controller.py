from lecture_view import View
from leture_model import Model

my_view = View()

my_model = Model("employees.db")

running = True

while running == True:
	user_input = my_view.mainMenu()

	if user_input == "1":
		name = my_view.takeInput("Enter your name: ")
		address = my_view.takeInput("Enter your address: ")
		ssn = my_view.takeInput("Enter your SSN: ")

		my_model.insertPerson(name, address, ssn)

	elif user_input == "2":
		employees = my_model.selectAllPeople()

		for employee in employees:
			my_view.printEmployee(employee)

	elif user_input == "3":
		employee_id = my_view.takeInput("Enter an employee's ID: ")

		try:
			employee_id = int(employee_id)
			
			result = my_model.selectOnePerson(employee_id)

			if result == None:
				my_view.printOutput("Employee not found")
			else:
				my_view.printEmployee(result)


		except:
			my_view.printOutput("Not a valid number. try again.")

	elif user_input == "4":
		running = False
	else:
		my_view.printOutput("Invalid menu item. Try again")