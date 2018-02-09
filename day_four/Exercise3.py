
def intToBinary(number):
	binary = ""
	while number > 0:
		remainder = number % 2
		number = number // 2

		binary = str(remainder) + binary

	return binary

print( intToBinary(26) )