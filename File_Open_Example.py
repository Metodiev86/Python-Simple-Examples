try:
  with open("Test_File.txt") as myFile:
    print(myFile.read())
    print("файл")
except FileNotFoundError:
  print("Файла не е намерен!")