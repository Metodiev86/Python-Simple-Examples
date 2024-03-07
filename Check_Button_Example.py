from tkinter import *

def Display():
	if(x.get()==1):
		print("Вие сте съгласен")
	else:
		print("Вие НЕ сте съгласен")

window = Tk()

x = IntVar()

check_button = Checkbutton(window,
                           text="Аз съм съгласен",
                           font=("Ariel", 12),
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=Display,
                           fg="#00ff00",
                           bg="black",
                           activebackground="black",
                           activeforeground="#00ff00",
                           #Премхава чекбокс кутията и го превъща в натисна/ненатистнат бутон
                           #indicatoron=0
                           )

check_button.pack()
window.mainloop()