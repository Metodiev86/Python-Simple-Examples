#Проста програма илюстрираща използването на проенливи.
#Показват се простите Типове променливи в Python.

first_name = 'Стоян'
last_name = "Методиев"
full_name = first_name + last_name
full_name_Corect = first_name + " " + last_name
age = 37
inc_age = age + 1
height = 1.60
human = True
dog = False
print(first_name)
print('Здравей ' + first_name)
print(type(first_name))
print(full_name)
print(full_name_Corect)
print(type(age))
print('age = ' + str(age) + "; age + 1 = " + str(inc_age))
print("Моята възраст е: " + str(age))
print("Моята височина е: " + str(height) + "cm")
print(type(height))
print("Човек ли си: " + str(human))
print("Куче ли си: " + str(dog))
print(str(type(human)) + " " + str(type(dog)))
