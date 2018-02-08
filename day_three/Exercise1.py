
target = input("Enter a word: ")

with open("word.txt", "r") as textfile:
	lines = textfile.readlines()

	is_found = False

	for word in lines:

		if word.strip() == target:
			is_found = True

	if is_found == True:
		print(target)
	else:
		print("Not Found")