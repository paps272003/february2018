
word = input("Enter a word: ")

palindrome = True

for x in range( len( word ) ):
	
	opposite = (x+1) * -1

	if word[x] != word[opposite]:
		palindrome = False


print(palindrome)