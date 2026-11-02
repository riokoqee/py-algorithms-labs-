year = int(input("Type a leap year: "))

is_leap = (
	(year % 4 == 0)
		and
	(year % 100 != 0)
		or
	(year % 400 == 0)
)

if is_leap:
	print(f"{year} is a leap year!")
	print("Leap year contains 366 days!")
else:
	print(f"Unfortunataly {year} is not a leap year!")
	print("Regular year contains 365 days!")