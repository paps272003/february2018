#Create function mergeSort that takes a list and returns a sorted list
def mergeSort(starting_list):

	#Create a list that will hold a list of lists
	unsorted_list = []

	#Insert each value from starting_list into unsorted_list as a list
	for value in starting_list:
		unsorted_list.append( [value] )

	#Run our sort until unsorted_list only has one list in it
	while len(unsorted_list) > 1:

		#create a new list that willhold a more sorted version of the original list
		sorted_list = []

		#run through every other index in unsorted_list
		for index in range(0, len(unsorted_list), 2):

			#If index is the last index in unsorted_list
			if index == len(unsorted_list)-1:
				#Add that index to the sorted_list unchanged
				#because we do not have another list to merge it with
				sorted_list.append( unsorted_list[index] )

			#If the index is not the last index and it has an index we can merge it with
			else:
				#Create a new list that will hold the result of the merge
				new_list = []

				#This while loop is the actual merge
				#Run this while loop until both lists are completely empty
				while len(unsorted_list[index]) > 0 or len(unsorted_list[index+1]) > 0:

					#If the list at index is empty
					if len(unsorted_list[index]) == 0:
						#Add the first value of index+1 to the new list
						temp = unsorted_list[index+1].pop(0)
						new_list.append(temp)
						#Repeat until both lists are empty

					#If the list at index+1 is empty
					elif len(unsorted_list[index+1]) == 0:
						#Add the first value at index to the new lists
						temp = unsorted_list[index].pop(0)
						new_list.append(temp)
						#Repeat until both lists are empty

					#If the first value of the list at index is less than or equal to
					#the first value of the list at index+1
					elif unsorted_list[index][0] <= unsorted_list[index+1][0]:
						#Add the first value of the list at index to the new list
						#and remove it from the list at index
						temp = unsorted_list[index].pop(0)
						new_list.append(temp)

					#If the first value of the list at index+1 is less than
					#the first value of the list at index
					elif unsorted_list[index][0] > unsorted_list[index+1][0]:
						#Add the first value of the list at index+1 to the new list
						#and remove it from the list at index+1
						temp = unsorted_list[index+1].pop(0)
						new_list.append(temp)

				#After merging the two lists add the result to the sorted list
				sorted_list.append(new_list)

		#Once all merges are complete set unsorted_list to sorted_list
		#If unsorted_list has more than one list the while loop will continue
		unsorted_list = sorted_list

	#Return the result of the completed while loop
	return unsorted_list[0]

mergeSort( [10,15,1,-7,8,10] )