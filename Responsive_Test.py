import tkinter as tk
from tkinter import ttk

# Дефиниране на основния прозорец
root = tk.Tk()
root.title("Адаптивно приложение")

# Адаптивен дизайн
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

# Определяне на минималния размер
root.minsize(width=400, height=300)

# Добавяне на съдържание
label = ttk.Label(frame, text="Адаптивно приложение")
label.grid(row=0, column=0)

button = ttk.Button(frame, text="Натисни ме!")
button.grid(row=1, column=0)

# Стартиране на приложението
root.mainloop()