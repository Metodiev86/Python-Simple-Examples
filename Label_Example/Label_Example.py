#'label' - е widget който съдържа текст и/или картинка в себе си и е закачен за window

from tkinter import *

window = Tk()
window.geometry("640x480")

photo = PhotoImage(file="label_icon.png")

label = Label(window,
              text="Hello",
              font=("Arial", 40, "bold"),
              fg='yellow',
              bg='#00ff00',
              image=photo,
              compound="bottom"
              )

#label.pack() #Задължителна функция, за показване на нашия 'label', по подразбиране го слага горе, централно

label.place(x= 0, y=0) #подаваме кордиати, къде да се появи нашия 'label'

window.mainloop()