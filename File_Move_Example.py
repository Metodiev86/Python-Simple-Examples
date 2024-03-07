import os
location = "Test_File2.txt"
destination = "E:\Stoqn\Programirane\Python\Examples_New\My_Folder"
try:
	if os.path.exists(destination):
		print("Файла вече съществува")
	else:
		os.replace(location, destination)
		print(destination + " e преместен")
except FileNotFoundError:
	print(location+" не е намерен!")