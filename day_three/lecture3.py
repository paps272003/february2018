
numbers = [1,2,3,4,5,6,7,8,9,10]

index = 0
#While the index is less than the length of the list
while index < len(numbers):
	#If the number at the current index is divisible by 2
	if numbers[index]%2 == 0:
		#remove it from the list
		numbers.pop(index)
	else:
		#If it is not divisible increase index by 1
		index = index +1

	print(numbers,index)


with open("test.txt", "r") as textfile:
	lines = textfile.readlines()

	for line in lines:

		print( line.strip() )


with open("test2.txt", "w") as writefile:
	writefile.write("Will be written to a file\n")
	writefile.write("JUST LIKE THIS")