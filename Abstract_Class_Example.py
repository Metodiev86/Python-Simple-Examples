#Абстрактните класове, са класове които съдържат един или повече методи които имат декларация, но нямат имплементация.
#Задължително трябва да се имплементират в класове наследници.

from abc import ABC, abstractmethod

class Vehicle(ABC):

	@abstractmethod
	def go(self):
		pass

	def Stop(self):
		pass

class Car(Vehicle):
	def go(self):
		print("Car is go!")

class Motorcicle(Vehicle):
	def go(self):
		print("Motorcicle go!")

	def Stop(self):
		print("Motorcicle Stoped!")

car = Car()
car.go()

motor = Motorcicle()
motor.Stop()