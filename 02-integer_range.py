n = int(input("How many bits: "))

min = -2 ** (n - 1)
max = (2 ** (n - 1)) - 1

print(f"{n}-bit two's complement range: [{min}, {max}]")