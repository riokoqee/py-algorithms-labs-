import sys

def checkNumber():

	number = int(input("Type a number: "))

	check = number % 2

	if check != 0:
		print(f"{number} is an odd number!")
		sys.exit()
	else:
		print("Your number is even!")
		checkNumber()

checkNumber()
