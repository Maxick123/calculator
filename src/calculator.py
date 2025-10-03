import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        self.current_input = ""
       
        self.create_widgets()
        
    def create_widgets(self):
     
        self.entry = tk.Entry(self.root, font=('Arial', 14), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='ew')
  
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row = 1
        col = 0
        for button in buttons:
            tk.Button(
                self.root, text=button, font=('Arial', 12),
                command=lambda b=button: self.button_click(b)
            ).grid(row=row, column=col, padx=5, pady=5, sticky='ew')
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        
        tk.Button(
            self.root, text='C', font=('Arial', 12),
            command=self.clear
        ).grid(row=row, column=0, columnspan=4, padx=5, pady=5, sticky='ew')
        
        
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def button_click(self, value):
        if value == '=':
            self.calculate()
        else:
            self.current_input += str(value)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.current_input)
    
    def calculate(self):
        try:
            
            if '+' in self.current_input:
                numbers = self.current_input.split('+')
                result = float(numbers[0]) + float(numbers[1])
            elif '-' in self.current_input:
                numbers = self.current_input.split('-')
                result = float(numbers[0]) - float(numbers[1])
            else:
                result = self.current_input
                
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
            self.current_input = str(result)
            
        except Exception as e:
            messagebox.showerror("Ошибка", "Некорректный ввод")
            self.clear()
    
    def clear(self):
        self.entry.delete(0, tk.END)
        self.current_input = ""

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()