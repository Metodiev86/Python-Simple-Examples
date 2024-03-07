from tkinter import *

food = ['pizza', 'hamburger', 'hotdog']


window = Tk()

def order():
	if(x.get()==0):
		print("Вие поръчахте ПИЦА")
	elif(x.get()==1):
		print("Вие поръчахте ХАМБУРГЕР")
	elif(x.get()==2):
		print("Вие поръчахте ХОТ-ДОГ")
	else:
		print("???")

pizzaImage = PhotoImage(file="pizza.png")
hamburgerImage = PhotoImage(file="hamburger.png")
hotdogImage = PhotoImage(file="hotdog.png")

foodImage = [pizzaImage, hamburgerImage, hotdogImage]
x = IntVar()

for index in range(len(food)):
	radiobuuton= Radiobutton(window,
	                         text=food[index],
	                         # добавя радиобутоните в една група, ако споделят една променлива
	                         variable=x,
	                         #присвоява стойност, с която се различава от другите радиобутони
	                         value=index,
	                         #Добавя разстояние от очертанията на елемента, по оста Х
	                         padx=25,
	                         # Добавя разстояние от очертанията на елемента, по оста Y
	                         pady=5,
	                         image=foodImage[index],
	                         font=("Ariel, 15"),
	                         compound="left",
	                         command=order

	                         )
	radiobuuton.pack(anchor=W) #Закотвяме бутоните на 'запад'
window.mainloop()