
class View:

	def takeInput(self, prompt):
		return input( prompt )

	def printOutput(self, output):
		print(output)

	def mainMenu(self):
		print("1. Enter an employee")
		print("2. View all employees")
		print("3. View employee by ID")
		print("4. Exit")

		return input("Enter a number")

	def printEmployee(self, employee):
		print(employee[0],"|",employee[1],"|",employee[2],"|",employee[3])