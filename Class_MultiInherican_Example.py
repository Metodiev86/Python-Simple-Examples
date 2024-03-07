class Organisam:
	 alive = True

class Animal(Organisam):
	def Eat(self):
		print("Животното яде")

class Dog(Animal):
	def Bark(self):
		print("Кучето Лае!!")

dog = Dog()

print("Кучето е живо: ", dog.alive)
dog.Eat()
dog.Bark()