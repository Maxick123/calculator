import tkinter as tk
from tkinter import messagebox

class Calculator
    def __init__(self, root)
        self.root = root
        self.root.title(Калькулятор)
        self.root.geometry(300x400)
        self.root.resizable(False, False)
        
        # Создаем интерфейс
        self.create_widgets()
        
    def create_widgets(self)
        # Поле ввода
        self.entry = tk.Entry(self.root, font=('Arial', 14), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='ew')
        
        # Кнопки
        buttons = [
            '7', '8', '9', '',
            '4', '5', '6', '',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row = 1
        col = 0
        for button in buttons
            tk.Button(
                self.root, text=button, font=('Arial', 12),
                command=lambda b=button self.button_click(b)
            ).grid(row=row, column=col, padx=5, pady=5, sticky='ew')
            col += 1
            if col  3
                col = 0
                row += 1
        
        # Кнопка очистки
        tk.Button(
            self.root, text='C', font=('Arial', 12),
            command=self.clear
        ).grid(row=row, column=0, columnspan=4, padx=5, pady=5, sticky='ew')
        
        # Настройка веса колонок для растягивания
        for i in range(4)
            self.root.grid_columnconfigure(i, weight=1)
    
    def button_click(self, value)
        print(fНажата кнопка {value})  # Заглушка
    
    def clear(self)
        print(Очистка)  # Заглушка

if __name__ == __main__
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()