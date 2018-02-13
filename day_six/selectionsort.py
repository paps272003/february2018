def selectionSort(starting_list):
	new_list = []

	while len(starting_list) > 0:

		print(starting_list, new_list)

		lowest_index = 0

		for index in range(0,len(starting_list)):

			if starting_list[index] < starting_list[lowest_index]:
				lowest_index = index

		removed_value = starting_list.pop(lowest_index)
		new_list.append(removed_value)

	return new_list

print( selectionSort( [10,15,1,-7,8,10,108] ) )