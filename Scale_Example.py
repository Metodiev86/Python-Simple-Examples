from tkinter import *

def Submit():
	print(f"Температурата е {scale.get()} °C")

window = Tk()

#скалата ще започва от горе на долу
#scale = Scale(window, from_=0, to=100)

scale = Scale(window,
              from_=100, #Начална стойност
              to=0, #Крайна Стойност
              length=600, #Дължината на скалата
              orient= VERTICAL, #Ориентацията мопже да бъде и хоризонтална
              font=("Consolas", 20),
              tickinterval=10, #Изобразява скала, през даден интервал
							showvalue=0, #скрива моментната стойност
              troughcolor="Blue", #Променя цвета на слайдъра
              fg="#FF1C00", #Променя цветът на шрифта
              bg="Black", #Променя цвета на фона
              )
scale.set(50) #Подаваме стойност която да е по подразбиране
scale.pack()

button = Button(window, text="submit", command=Submit)
button.pack()
window.mainloop()