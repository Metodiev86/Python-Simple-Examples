
def hello():
    print("hello")

hello()

def multiply(number1, number2):
    return number1 * number2

x = multiply(6.5, 8)
print(x)

def hello_name(name, middle, lastname):
    print("hello" + " " + name + " " + middle + " " + lastname)

hello_name("Stoqnov", "Metodi",  "Metodiev")
hello_name(middle="Stoqnov", name="Metodi", lastname="Metodiev")