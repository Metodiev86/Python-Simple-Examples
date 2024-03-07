from tkinter import *
from tkinter import filedialog

def SaveFile():
	file = filedialog.asksaveasfile(defaultextension=".txt",
	                                filetypes=[
		                                ("Text file *.txt", ".txt"),
		                                ("HTML file *.html", "*.html"),
		                                ("All file *.*", "*.*"),
	                                ])
	if file is None: #Предотвратява ексепшен, че няма подаден файл
		return
	fileText = str(text.get(1.0, END))
	file.write(fileText)
	file.close()

window = Tk()

saveButton = Button(window, text="Save", command=SaveFile)
saveButton.pack()

text = Text(window)
text.pack()

window.mainloop()