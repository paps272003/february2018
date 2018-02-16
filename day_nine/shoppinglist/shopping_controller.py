from shopping_model import Model
from shopping_view import View

my_model = Model()

my_view = View()

running = True

while running == True:

	choice = my_view.mainMenu()

	if choice == "1":

		item_name = my_view.takeInput("Enter an item to add to the list: ")

		my_model.insertItem(item_name)

	elif choice == "2":

		all_items = my_model.selectAllItems()

		for item in all_items:
			my_view.printItem(item)

	elif choice == "3":

		item_id  = my_view.takeInput("Enter an item id to check off: ")

		try:
			item_id = int(item_id)

			exists = my_model.checkId(item_id)

			if exists == None:
				my_view.printOutput("Item id does not exist")
			else:
				my_model.updateChecked(item_id, "CHECKED")
		
		except:
			my_view.printOutput("Not a number, try again")

	elif choice == "4":

		item_id  = my_view.takeInput("Enter an item id to uncheck: ")

		try:
			item_id = int(item_id)

			exists = my_model.checkId(item_id)

			if exists == None:
				my_view.printOutput("Item id does not exist")
			else:
				my_model.updateChecked(item_id, "UNCHECKED")
		
		except:
			my_view.printOutput("Not a number, try again")


	elif choice == "5":
		running = False
	else:
		my_view.printOutput("Invalid menu item. Try again.")

