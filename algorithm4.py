n_fr = int(input("Number of friends: "))
s_piz = int(input("Slices per pizza: "))
s_fr = int(input("Slices per friend: "))

slices_total = n_fr * s_fr
order = (slices_total + n_fr) % s_piz
print(slices_total, order)