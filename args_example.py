#'*args' указва на функцията, че е с променлив брой параметри.
# Tuple от аргументи, което означава, че са непроменими. 'args',
# не е задължително име, може да се кrъсти всякак, задължително трябва да е предхождано от '*'

def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)

add(1,2,3,4)
add(1,2,3,4,5,6)

#Заобикаляме правилото за непроменими стойности, като преобразуваме 'args' от 'Tuple' в 'List'
def add1(*args):
    sum = 0
    stuff = list(args)
    stuff[0] = 0
    for i in stuff:
        sum += i
    print(sum)
add1(1,2,3,4)
add1(1,2,3,4,5,6)