#"**kwargs", пак оказва че функцията е с променлив брой параметри, но ги превръща в речник.
# Двойка ключ : стойност

myname = "Valeria"
mymiddle_name = "Stoqnova"
myLast_name = "Metodieva"

def hello_name(**kwargs):
    print("hello ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello_name(name = myname, midlename = mymiddle_name, last_name = myLast_name)

def hello_name_title(**kwargs):
    print("Hello")
    for key, value in kwargs.items():
        print(value, end=" ")

hello_name_title(title = "Uchenichkata", name = "Mihaela", middlename = "Stoqnova", last_name = "Metodieva")