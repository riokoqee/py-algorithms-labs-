n = int(input("Type a number that is less 1000: "))
if 0 <= n <= 999:
	first = n // 100
	second = (n % 100) // 10
	third = n % 10
	print(first, second, third)
else:
	print("Number is incorrect!")