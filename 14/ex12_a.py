import tkinter as tk
class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Expression Calculator")
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(master, textvariable=self.input_var)
        self.input_entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.result_label = tk.Label(master, textvariable=self.result_var, width=20)
        self.result_label.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        row = 2
        col = 0
        for button_text in self.buttons:
            tk.Button(master, text=button_text, width=5, command=lambda x=button_text: self.button_click(x)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1
        tk.Button(master, text='Clear', width=5, command=self.clear).grid(row=row, column=0, columnspan=2, padx=5, pady=5)
        tk.Button(master, text='Quit', width=5, command=master.quit).grid(row=row, column=2, columnspan=2, padx=5, pady=5)
    def button_click(self, text):
        if text == '=':
            result = str(eval(self.input_var.get()))
            self.result_var.set(result)
            self.input_var.set(result)
        elif text == 'Clear':
            self.clear()
        else:
            self.input_var.set(self.input_var.get() + text)

    def clear(self):
        self.input_var.set('')
        self.result_var.set('0')
root = tk.Tk()
my_gui = CalculatorGUI(root)
root.mainloop()
