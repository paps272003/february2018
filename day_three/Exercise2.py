with open("letters.txt", "r") as textfile:
	letters = textfile.readline()

	letter_dict = {}

	for letter in letters:

		if letter in letter_dict:
			letter_dict[letter] = letter_dict[letter] + 1

		else:
			letter_dict[letter] = 1

	for key in letter_dict.keys():
		print(key, letter_dict[key])