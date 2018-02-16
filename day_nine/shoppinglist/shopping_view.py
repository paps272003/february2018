
class View:

	def takeInput(self, prompt):
		return input( prompt )

	def printOutput(self, output):
		print(output)

	def mainMenu(self):
		print("1. Enter an item")
		print("2. View list")
		print("3. Check off item")
		print("4. Uncheck item")
		print("5. Exit")

		return input("Enter a number")

	def printItem(self, item):

		print(item[0],'|',item[1],"|",item[2])