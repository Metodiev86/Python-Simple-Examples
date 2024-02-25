menu = {"pizza": 3.00,
        "popcorn": 5.00,
        "chips": 3.5,
        "cola": 2.00,
        "fanta": 2.00}

cart = []
total = 0

print("-"*7,"MENU","-"*7)
for key, value in menu.items():
	print(f"{key:10}: {value:.2f} лв.")
print("-"*20)

while True:
	choyse = input("Изберете от менюто, (за изход натиснете q): ").lower()
	if choyse == "q":
		break
	elif menu.get(choyse) is not None:
		cart.append(choyse)
print("-" * 50)

print(cart)

for food in cart:
	total += menu.get(food)
print("-"*50)
print(f"СУМА: {total:.2f} лв.")

