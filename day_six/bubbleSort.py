
#Create bubbleSort function that takes a list and sorts it
def bubbleSort(starting_list):

	#Define the variable swapped
	#Swapped will hold if we have made a swap in this loop or no swaps in this loop
	swapped = True

	#Run this loop until we have made a full iteration and made no swaps in the iteration
	while swapped == True:

		#Start swapped as false
		#Swapped will stay false until a swap has been made
		swapped = False

		#Iterate through each index in the list
		for index in range(0, len(starting_list)-1):
			
			# print(starting_list)
			
			#Compare each index against the next index and check if we need to swap the indexes
			if starting_list[index] > starting_list[index+1]:

				#Single line swap code
				# starting_list[index], starting_list[index+1] = starting_list[index+1], starting_list[index]
				
				#Multiple line swap code
				#Start by creating a variable I call temp. Set temp equal to one value from the swap
				temp = starting_list[index]

				#Then replace the value we just put in temp with the other value of the swap
				starting_list[index] = starting_list[index+1]

				#Set the value of the other value to temp
				starting_list[index+1] = temp

				#I have made a swap so swapped is now true
				swapped = True

		#If through the for loop we have made no swaps then the list is sorted and the while loop will end

		# print("------------")

	return starting_list

print( bubbleSort( [10,15,1,-7,8,10,108] ) )