#Библиотеката 'tkinter' е вградена в python, за изграждане на графичен интерфейс:
#widgets - елемнти на потребителския интерфейс (бутоно, етилети, падащи списъци и т.н.)
#windows - контейнери които съдържа и държат в себе си 'widgets'

from tkinter import *

window = Tk() #Тук правим инстанция на нашия window

window.geometry("640x640")
window.title("Първата ми GUI програма")

icon = PhotoImage(file="fresh.png")
window.iconphoto(True, icon)
window.config(background="Blue")

window.mainloop() #Тук показваме нашия window

