string = input("Enter 3-digit integer: ")

if len(string) == 3:
	print(string[0:1], string[1:2], string[2:3])
else:
	print("Input is incorrect!")