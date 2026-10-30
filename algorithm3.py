import math

number = int(input("Enter a radius: "))
radius = float(number)
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"Circumference of a circle of radius {radius} is {circumference}")
print(f"Area of a circle of radius {radius} is {area}") # area output