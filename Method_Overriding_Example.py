class Animal:
	def Eat(self):
		print("Животното яде!")

class Rabit(Animal):
	def Eat(self):
		print("Заекът яде морков!")

rabit = Rabit()
rabit.Eat()