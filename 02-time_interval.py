first = int(input("Enter the first time (e.g., 0930): "))
second = int(input("Enter the second time (after the first): "))

first_hour = first // 100
second_hour = second // 100

first_min = first % 100
second_min = second % 100

if not (0 <= first_hour <= 23) or not (0 <= second_hour <= 23) or not (0 <= first_min <= 59) or not (0 <= second_min <= 59):
    print("Incorrect time!")
else:
	first_total = (first_hour * 60) + first_min
	second_total = (second_hour * 60) + second_min
	
	total = second_total - first_total
	if total <= 0:
		print("Incorrect input!")
	else:
		hours = total // 60
		minutes = total % 60

		hour_word = "hours"
		min_word = "minutes"
		if hours == 1:
			hour_word = "hour"
		if minutes == 1:
			min_word = "minute"

		print(f"Elapsed time: {hours} {hour_word} and {minutes} {min_word}.")

