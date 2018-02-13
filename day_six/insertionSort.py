#Create function for insertion sort. This takes in a list to be sorted
def insertionSort(starting_list):

	#Index is the current index we are comparing and sorting
	index = 0

	#Run the code until every index has been sorted
	while index < len(starting_list):

		print(starting_list)
		#FOr each index check every index before it
		for back_index in range(index,-1,-1):
			#If the value at index is greater than the value at back_index
			if starting_list[index] > starting_list[back_index]:
				#insert the value at index after back_index
				temp_value = starting_list.pop(index)
				starting_list.insert( back_index+1, temp_value )
				#Once we find the value to insert after end the for loop
				break
			#If the value at index is less than all other values and back index is the last index
			elif back_index == 0 and starting_list[index] < starting_list[back_index]:
				#Insert the value at the begining of the list
				temp_value = starting_list.pop(index)
				starting_list.insert(0, temp_value)

		#After sorting index move on the the next index
		index = index + 1

	#WHen the while loop finishes return the sorted list
	return starting_list

print( insertionSort( [10,15,1,-7,8,10,108] ) )