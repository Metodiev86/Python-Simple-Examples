class Rectangle:
	def __init__(self, lenght, widht):
		self.lenght = lenght
		self.widht = widht

class Square(Rectangle):

	def __init__(self, lenght, widht):
		super().__init__(lenght, widht)

	def Area(self):
		return self.lenght*self.widht

class Cube(Rectangle):
	def __init__(self, lenght, widht, hight):
		super().__init__(lenght,widht)
		self.hight = hight

	def Volume(self):
		return self.hight*self.widht*self.lenght

square = Square(3,3)

cube = Cube(2,2,2)

print(square.Area())
print(cube.Volume())