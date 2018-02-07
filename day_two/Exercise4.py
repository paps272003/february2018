
length = 101

midpoint = (length+1) // 2

for height in range(1,length+1):

	#Print stars ascending until the midpoint is passed
	if height <= midpoint:
		for width in range(height):
			#Print a star and do not move to the next line
			print("*", end="")

		print()

	#Once midpoint is passed begin descending
	else:
		#Calculate the number of stars needed according to the current height and the length
		stars = (length - height) + 1
		for width in range(stars):
			#Print a star and do not move to the next line
			print("*", end="")

		print()

