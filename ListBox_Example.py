from tkinter import *

food = ["Soup", "Salad", "Desert", "Breath", "Cola"]

def Submit():
	selected_food = []
	for index in listbox.curselection():
		selected_food.insert(index, listbox.get(index))
	for i in selected_food:
		print(i)
window = Tk()

def Add():
	new_item = textBox.get()
	listbox.insert(listbox.size(), new_item)
	listbox.config(height=listbox.size())

def Delete():
	for index in reversed(listbox.curselection()):
		listbox.delete(index)
	listbox.config(height=listbox.size())

def Clear():
	listbox.delete(0, listbox.size())


listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("constantia, 35"),
                  width=10,
									#Дава право на селектиране на повече от един елемент
                  selectmode=MULTIPLE
									#Дава на избор на повече от един елемент. Маркира се чрез плъзване
									#selectmode=EXTENDED
                  #Единичен избор на елемент
                  #selectmode= SINGLE
                  #Избор на само един елемент, но поддържа плъзване на мишката
                 #selectmode=BROWSE
                  )
listbox.pack()

for index in range(len(food)):
	listbox.insert(int(index), food[index])

#Тази функция автоматично ораязмерява полето, зависи колко записа има в него
listbox.config(height=listbox.size())


textBox = Entry(window)
textBox.pack()

submitButton = Button(window, text="Submit", command=Submit)
submitButton.pack()

addButton = Button(window, text="Add", command=Add)
addButton.pack()

deleteButton = Button(window, text="Delete", command=Delete)
deleteButton.pack()

clear_button = Button(window, text="Clear", command=Clear)
clear_button.pack()

window.mainloop()