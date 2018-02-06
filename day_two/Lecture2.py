
#LISTS

names = ["MAtthew", "Tim"]

print(names)

names.append("Sun")

print(names)

names.insert(2 , "Anthony")

print(names)

names[0] = "Matthew"

print(names)

names.pop(0)

print(names)

print( names[0] )


#DICTIONARIES

SSN = { "12345":"Matthew", "12346":"Anthony" }

print(SSN)

SSN["12347"] = "Sun"

print(SSN)

del SSN["12347"]

print(SSN)


#for loop

for name in names:
	print(name)
	name = "BLANK"

for x in range( len(names) ):
	print(x)
	print( names )

	names[x] = "BLANK"

print(names)