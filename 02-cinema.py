age = int(input("Age: "))
ticket = input("Do you have a ticket? (yes/no): ")
accompany = input("Are you accompanied by an adult? (yes/no): ")

has_ticket = (ticket == "yes")
has_accompany = (accompany == "yes")

can_enter = (
	(age >= 14 and has_ticket)
		or 
	(age < 14 and has_accompany and has_ticket)
		or 
	(age > 65)
)

print(f"Can enter: {can_enter}")