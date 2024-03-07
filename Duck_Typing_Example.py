class Duck:
	def Walk(self):
		print("Патката ходи!")

	def Speek(self):
		print("Патката кряка!")


class Chiken:
	def Walk(self):
		print("Пилето ходи!")

	def Speek(self):
		print("Пилето кудкудяка!")

class Person():

	def catch(self, duck):
		duck.Walk()
		duck.Speek()
		print("Хванахте същството!")

duck = Duck()
chiken = Chiken()
person = Person()

person.catch(duck)


person.catch(chiken)
