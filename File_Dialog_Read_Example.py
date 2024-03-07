from tkinter import *
from tkinter import filedialog

def openFile():
	filepath = filedialog.askopenfilename(initialdir="File_Dialog",
																				title="Отвори файл",
	                                      filetypes=(("Text files *.txt","*.txt"),
	                                                 ("All files *.*", "*.*"))
	)
	file = open(filepath, 'r')
	print(file.read())
	file.close()

window = Tk()

button = Button(window, text ="Open File", command=openFile)
button.pack()

window.mainloop()