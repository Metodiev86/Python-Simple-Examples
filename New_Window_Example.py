from tkinter import *

def New_Top_Window():
	#Top_level() - Обвързва новия прозорец, със своя създател (прозореца от който е създаден) и ако затворим създателя,
	# затваряме и  новия прозорец, но ако затоврим новия прозорец, не затваряме създателя (прозорец)
	new_top_window = Toplevel()

def New_Tk_Window():
	#Tk(), не обвързва новия прозорец, със своя създател.
	# Те са като два отделни елемента, без жизнена връзка между тях.
	new_tk_window = Tk()
	old_window.destroy()


old_window = Tk()

button = Button(old_window, text="Creat Top Window", command=New_Top_Window).pack()
button = Button(old_window, text="Creat Tk Window", command=New_Tk_Window).pack()
old_window.mainloop()