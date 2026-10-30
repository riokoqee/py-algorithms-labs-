n_fr = int(input("Number of friends: "))
s_piz = int(input("Slices per pizza: "))
s_fr = int(input("Slices per friend: "))
cost = int(input("Cost of a single pizza: "))

slices_total = n_fr * s_fr
order = slices_total // s_piz
extra_slices = slices_total % s_piz
if extra_slices > 0:
	order += 1
whole_slices = order * s_piz
remainder = whole_slices - slices_total
total_cost = cost * order
print(f"Total slices: {slices_total}")
print(f"Amount of pizza to order: {order}")
print(f"Remainder: {remainder}")
print(f"Total cost: {total_cost}")