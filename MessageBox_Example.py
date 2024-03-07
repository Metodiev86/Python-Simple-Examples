from tkinter import *
from tkinter import messagebox

def Info_Message():
	messagebox.showinfo(title="Информационно съобщение!", message="Ти си човек!")

def Warning_Message():
	messagebox.showwarning(title="Warning", message="Внимание")

def okCancel_Message():
	if messagebox.askokcancel(title="Ok or Cancel", message="Съгласни ли сте да продължите"):
		print("Браво продължавате!")
	else:
		print("Вие се отказахте :(")

window = Tk()

info_button = Button(window, text="Info", command=Info_Message)
info_button.pack()

warning_button = Button(window, text="Warning", command=Warning_Message)
warning_button.pack()

okCancel_button = Button(window, text="Ok or Cancel", command=okCancel_Message)
okCancel_button.pack()

window.mainloop()
