#filter() - създава колекция от итериращи елемнти, за които дадена функция връща True
#
#filter(function, iterable) - приема два аргумента, функция и итериращ елемент

big_famyly = [("Metodi", 58),
              ("Atanaska", 57),
							("Denka", 80),
							("Vasilka", 83),
							("Stoyan", 37),
							("Valq", 14),
							("Stela", 27),
							("Darina", 39),
							]

young_age = lambda data:data[1]<=40
young_family = list(filter(young_age, big_famyly))

old_age = lambda data: data[1]>=40
old_family = list(filter(old_age, big_famyly))

for i in young_family:
	print(str(i) + ", ", end="")
print()

for i in old_family:
	print(str(i) + ", ", end="")