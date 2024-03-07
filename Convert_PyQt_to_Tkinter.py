import tkinter as tk
from tkinter import ttk

class FreshForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("271x600")
        self.title("Fresh_form")

        self.init_ui()

    def init_ui(self):
        # Frame for buttons and combobox
        self.frame = tk.Frame(self, height=80)
        self.frame.pack(fill=tk.X, pady=20)

        # Buttons
        self.show_button = tk.Button(self.frame, text="Заявка", command=self.show_button_click)
        self.show_button.pack(side=tk.LEFT)

        self.read_button = tk.Button(self.frame, text="Преглед", command=self.read_button_click)
        self.read_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(self.frame, text="Изтрий", command=self.delete_button_click)
        self.delete_button.pack(side=tk.LEFT, padx=10)

        # Listview
        self.listview = tk.Listbox(self, font=("Candara", 12, "bold"), height=12)
        self.listview.pack(fill=tk.BOTH, pady=10)

        # Combobox
        self.combobox = tk.ttk.Combobox(self.frame, font=("Candara", 11, "bold"), width=20)
        self.combobox.pack(side=tk.RIGHT, padx=10)

        # Checkboxes
        self.checkbox_all = tk.Checkbutton(self.frame, text="Всички")
        self.checkbox_all.pack(side=tk.RIGHT)

        # Frame for quantity and add button
        self.frame_bottom = tk.Frame(self, height=80)
        self.frame_bottom.pack(fill=tk.X, pady=10)

        # Quantity textbox
        self.quantity_textbox = tk.Entry(self.frame_bottom, font=("Arial", 11, "bold"), width=6)
        self.quantity_textbox.pack(side=tk.LEFT)

        # Checkbox for quantity
        self.checkbox_quantity = tk.Checkbutton(self.frame_bottom, text="Кашон/Стек")
        self.checkbox_quantity.pack(side=tk.LEFT, padx=10)

        # Add button
        self.add_button = tk.Button(self.frame_bottom, text="Добави", command=self.add_button_click)
        self.add_button.pack(side=tk.LEFT, padx=10)

        # Checkbox for percentage
        self.checkbox_percentage = tk.Checkbutton(self.frame_bottom, text="+%")
        self.checkbox_percentage.pack(side=tk.LEFT)

    # Button click handlers
    def show_button_click(self):
        # Implement your functionality for the show button
        pass

    def read_button_click(self):
        # Implement your functionality for the read button
        pass

    def delete_button_click(self):
        # Implement your functionality for the delete button
        pass

    def add_button_click(self):
        # Implement your functionality for the add button
        pass

if __name__ == "__main__":
    app = FreshForm()
    app.mainloop()
