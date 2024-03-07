class Car:

	def Turn_ON(self):
		print("Start")
		return self

	def Drive(self):
		print("Drive")
		return self

	def Break(self):
		print("Break")
		return self

	def Turn_OFF(self):
		print("Stop")
		return self

car = Car()

car.Turn_ON().Drive().Break().Turn_OFF()

