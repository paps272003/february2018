small_bottles = input("How many small bottles: ")
large_bottles = input("How many large bottles: ")

total = int(small_bottles)*0.1 + int(large_bottles) * 0.25

print( "Your total is {:.2f}".format(total) )