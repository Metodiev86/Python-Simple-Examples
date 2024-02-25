# "Tuple" е подобна структора на лист, с разликата, че са непроменими и подредени.
# Неможем да ги променяме след тяхната инциализация

student = ("Валерия", 14, "жена", "Михаела", 14, "жена")

print(student)

count_name = student.count("Валерия")
count_age = student.count(14)

print(count_name) #Брои колко пъти се среща името Валерия
print(count_age) #Брои колко пъти се среща числото 14

index_element_name = student.index("Михаела")
print(index_element_name) #Отпечатва кой по ред елемент е "Михаела"

index_element_age = student.index(14)
print(index_element_age) #Отпечатва кой по ред е елемента '14', връща първото срещане