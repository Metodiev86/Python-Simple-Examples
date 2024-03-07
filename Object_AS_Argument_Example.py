class Car:
	color = None

car1 = Car()
car2 = Car()

print(car1.color)
print(car2.color)

def change_color(car, color):
	car.color = color

change_color(car1, "Red")
change_color(car2, "Blue")

print(f"Цветър на car1 e {car1.color}")
print(f"Цветър на car2 e {car2.color}")