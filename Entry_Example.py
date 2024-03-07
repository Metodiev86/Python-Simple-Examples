from tkinter import *
def Submit():
	username = entry.get()
	print("Hello " + username)
	entry.config(state=DISABLED) #Когато използваме тази функция и полето вече не е достъпно

def Delete():
	entry.delete(0, END)

def Backspace():
	entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window,
              font=("Arial", 30),
              fg="#00ff00",
              bg="Black",
              #show="*" #Избираме какъв знакл да се показва вместо нашите символи (подходящо за пароли)
              )
entry.pack(side="left")

submit_button = Button(window, text='Submit', command=Submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text='Delete', command=Delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text='Backspace', command=Backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()