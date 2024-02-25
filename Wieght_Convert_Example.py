try:
	my_Weight = float(input("Въведете вашето тегло: "))
except ValueError:
	print("Само числа може за вход")
if(my_Weight<0):
	print("Теглото не може да е отрицателна стойност")
unit = input("В каква мерна единица е. K за килограм и L за паунд: ")
if unit == "k":
	my_Weight = round(my_Weight * 2.025, 1)
	unit = "килограма"
	print(f"Вашето тегло е {my_Weight} {unit}")
elif unit == "l":
	my_Weight = round(my_Weight/2.025, 1)
	unit = "паунда"
	print(f"Вашето тегло е {my_Weight} {unit}")
else:
	print("Може да изберете само K или L")
