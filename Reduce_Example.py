#reduce() - функция която приема два аргумента, функция и итериращ елемент. Аргумента функция се повтаря, и натрупва
# стойностите, докато не остане само един елемент

import  functools
digits = (10, 12 , 15, 13, 5)

result_digits = functools.reduce(lambda x,y: x+y, digits)
print(result_digits)

word = ("H","E","L","L","O")

result_word = functools.reduce(lambda x,y: x+y, word)
print(result_word)