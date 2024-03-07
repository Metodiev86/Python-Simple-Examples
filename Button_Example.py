from tkinter import *

count = 0
def Click():
  global count
  count += 1
  print(count)

window = Tk()

photo = PhotoImage(file="FileNotExist.png")

button = Button(window,
                text="Cliked me",
                command=Click,
                font=("Times New Roman", 14, "bold"),
                fg="#00ff00",
                bg="Black",
                image=photo,
                compound="bottom"
                )

button.pack()
button.place(x=0,y=0)

window.mainloop()