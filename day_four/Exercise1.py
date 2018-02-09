
def findWord(target):

	with open("word.txt", "r") as textfile:
		lines = textfile.readlines()

		is_found = False

		for word in lines:

			if word.strip() == target:
				is_found = True

		return is_found


print( findWord("hello") )