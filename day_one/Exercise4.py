letter = input("Enter a letter: ")

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
	print("VOWEL")
elif letter == "y":
	print("Either vowel or consonant")
else:
	print("CONSONANT")