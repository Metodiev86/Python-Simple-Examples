#Sort е моетод който е към структората Лист
#Sort като функция, работи върху други итериращи елемнти, връща нареден лист
#Ако променливата е TUPLE, ще даде грешка, трябва да я подадем на функцията 'sorted()', не е като вграден метод

family = ["Стоян", "Стела", "Валерия", "Михаела", "Анна"]

family.sort()

for item in family:
	print(item + ", ", end="")
print()
#Приема два незадължителни аргумента 'key=' и 'reverse='. 'reverse=' обръща елементите низходящ ред.
family.sort(reverse=True)

for item in family:
	print(item + ", ", end="")
print()

family = ("Валя", "Миша", "Стоян", "Стели", "Анни")

sorte_family = sorted(family)

for item in sorte_family:
	print(item + ", ", end="")
print()

student = [("Методи", "Ф", 58),
           ("Атанаска", "А", 57),
           ("Василка", "К", 58),
           ("Денка", "И", 58),
           ]

sorted_student = sorted(student)

for item in sorted_student:
	print(str(item) + ", ", end="")
print()


grade = lambda grade:grade[1]
sorted_student = sorted(student, key=grade)

for item in sorted_student:
	print(str(item) + ", ", end="")
print()


