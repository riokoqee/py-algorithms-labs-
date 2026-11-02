x = int(input("Type a number x: "))
a = int(input("Type a number a: "))
b = int(input("Type a number b >= a: "))

is_in_range = True

if a <= x and b >= x:
	is_in_range = True
else:
	is_in_range = False

msg = "x falls in range [a,b]:" # where x, a, and b are the entered values
print(msg, is_in_range)
