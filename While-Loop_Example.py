#Примери за използване на цикъл с оператора WHILE. В примера ще се изпълнява подкана за задаване на име,
# докато не попълним, някакво име, по голямо или равяно на 3 символа

name=""
while len(name) < 3:
    name = input("Въведете своето име: ")
