name = input("What is your name? ")
age = input("What is your age? ")
height = 6.1
middle_initial = 'C'

if int(age) >= 18:
	license = True
	
elif int(age) < 18:
	license = False

age = int( age ) + 5

print(age)

print(name)

print(license)