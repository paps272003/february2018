numbers = list( range(2,101) )

index = 0

while index < len(numbers):

	inner_index = index + 1

	while inner_index < len(numbers):
		if numbers[inner_index] % numbers[index] == 0:
			numbers.pop(inner_index)
		else:
			inner_index = inner_index + 1

	index = index + 1
print(numbers)