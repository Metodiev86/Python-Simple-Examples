#Пример за използването на Brack, Continue, Pass

while True:
    name = input("Въведете своето име: ")
    if name != "":
        break #"breack" пртекъсва цикъла
print(name)

phone = "0888-415-383"
for i in phone:
    if i == "-":
        continue # "continue" продължава цикъла, дори след някакво условие
    print(i, end="")
print()
for i in range(1,21):
    if i == 13:
        pass    #"Pass" не изпълнява нищо, може да се ползва като "пропусни (skip)"
    else:
        print(str(i) + " ",end="")