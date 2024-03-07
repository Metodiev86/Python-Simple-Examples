foods = []
prices = []
counts = []
total = 0

while True:
	food = input("Веведете име на храна. За изход натиснете 0 :")
	if food == "0":
		break
	else:
		while True:
			count = float(input("Веведете брой: "))
			if count <= 0:
				print("Бройката НЕ може да е отрицателна")
			else:
				while True:
					price = float(input(f"Въведете цена за {food}:  $"))
					if price < 0:
						print("Цената НЕ може да е отрицателна")
					else:
						foods.append(food)
						counts.append(count)
						prices.append(price)
						break
				break
print(foods)
print(prices)
print(counts)

for x , y in prices, counts:
	total = (x * y) + total

print("----- Твоята Поръчка --------")
for food, count, price in zip(foods, counts, prices):
	print(f"{food:10} {count:5} {price:10}")
print("-"*30)
print(total)
