#list_comprehension - суъздаване на нов лист с по-лесен синтаксис от ламбда функция.
#list -> [израз (if/else) за елемнтите които се итерират]

square = []
for i in range(1,11):
		square.append(i*i)
print(square)

square_comprehension = [i * i for i in range(1,11)]
print(square_comprehension)

student_ratting = [100,90,80,70,60,50,30,0]

student_chek = list(filter(lambda x: x>60, student_ratting))
print(student_chek)

student_pass = [i for i in student_ratting if i>60]
print(student_pass)

passed_student = [i if i>60 else "Failde" for i in student_ratting]
print(passed_student)