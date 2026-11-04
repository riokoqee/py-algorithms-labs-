import sys

try:
    x = int(input("Type x number: "))
except ValueError:
    try:
        x = int(input("Invalid number! Try again: "))
    except ValueError:
        print("Invalid number twice!")
        sys.exit()
try:
    low = int(input("Type low number: "))
except ValueError:
    try:
        low = int(input("Invalid number! Try again: "))
    except ValueError:
        print("Invalid number twice!")
        sys.exit()
try:
    high = int(input("Type high number: "))
except ValueError:
    try:
        high = int(input("Invalid number! Try again: "))
    except ValueError:
        print("Invalid number twice!")
        sys.exit()
if low > high:
	print("Incorrect input!")
else:
	if low <= x <= high:
		print(f"{x} is in range of {low} and {high}")
	else:
		print("Nope!")