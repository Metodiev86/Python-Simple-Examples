#grid - разпределя компонентите под вид на таблица, колоните са с размера на най-големия компонент в него

from tkinter import *

window = Tk()

firstName_label = Label(window, text="First Name: ", font=("ariel", 14)).grid(row=0, column =0)
firstName_Entry = Entry(window, font=("ariel", 14), width=15).grid(row=0, column=1)

lasttName_label = Label(window, text="Last Name: ", font=("ariel", 14)).grid(row=1, column =0)
lasttName_Entry = Entry(window, font=("ariel", 14), width=15).grid(row=1, column=1)

email_label = Label(window, text="E-mail: ", font=("ariel", 14)).grid(row=2, column =0)
email_Entry = Entry(window, font=("ariel", 14), width=15).grid(row=2, column=1)

#colmnspan - определя колко свободни колони да обхваща, след тази в която е разположен елемента
button = Button(window, text="Submit").grid(row=3, column=0, columnspan=2)
window.mainloop()