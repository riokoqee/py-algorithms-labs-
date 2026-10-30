n = int(input("Type a 3-digit number less or equal to 342: "))
b = int(input("Type a base more than 1 and less than 10: "))
if 0 <= n <= b ** 3 - 1 and 1 < b < 10:
	first = n // (b ** 2)
	second = (n % (b ** 2) // b)
	third = n % b
	print(f"The base was: {b} {first}{second}{third}")
else:
	print("A base or a number are incorrect!")