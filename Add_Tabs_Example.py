from tkinter import *
from tkinter import ttk
window = Tk()

#ttk.Notebook() - Управлява колекция от прозорци и дисплеи
notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="Tab1")
notebook.add(tab2, text="Tab2")
notebook.pack(expand=True, fill="both") #expand - Разширява се докато запълни всяко празно място
																				#fill запълва по оста x и оста y
Label(tab1, text="This Tab1", width=50, height=25).pack()
Label(tab2, text="Goodbay! This Tab2", width=50, height=25).pack()
window.mainloop()