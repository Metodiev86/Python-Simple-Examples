#"Използване на "List", мулти множество от елементи събрани в една променлива

food = ["Пица", "Ябълка", "Сладолед"]

#Отпечатва целия списък във суров вид
print(food)

#Достъп на елемнтите по индекс, индексацията започва от 0
print(food[1]) #Отпечатва 'Ябълка'

#Списъците са изменими, могат да се променят по всяко време:

food[1] = "Сок" #Променяме втория елемент от 'Ябълка' на 'Сок'
print(food[1]) #Вече ще отпечата 'Сок'

#Списъците са итеруими, могат да се опечатат в цикъл, техните елемнти. Един вид са днамични масиви.

for i in food:
    print(i + " ", end="")

