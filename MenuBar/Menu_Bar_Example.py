from tkinter import *
from tkinter import filedialog


def OpenFile():
	filedialog.askopenfiles()

def SaveFile():
	filedialog.asksaveasfile(defaultextension=".txt")

def Cut():
	print(f"Вие Избрахте: Cut")

def Copy():
	print(f"Вие Избрахте: Copy")

def Past():
	print(f"Вие Избрахте: Past")
window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

openIcon = PhotoImage(file="open.png")
saveIcon = PhotoImage(file="save.png")
exitIcon = PhotoImage(file="exit.png")

fileMenu = Menu(menubar, tearoff=0, font=("MV Boli",15))
menubar.add_cascade(label="File", menu=fileMenu,)
fileMenu.add_command(label="Open", command=OpenFile, image=openIcon, compound=LEFT)
fileMenu.add_command(label="Write", command=SaveFile, image=saveIcon, compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit, image=exitIcon, compound=LEFT)

editMenu = Menu(menubar, tearoff=0, font=("MV Boli",15))

menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=Cut)
editMenu.add_command(label="Copy", command=Copy)
editMenu.add_command(label="Past", command=Past)

window.mainloop()

