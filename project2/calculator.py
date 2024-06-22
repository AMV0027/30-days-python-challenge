import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value )

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()

root.title("Tkinter Calculator")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons =[
    ('0',1,0), ('1',1,1),('2',1,2),('/',1,3),
    ('3',2,0),('4',2,1),('5',2,2),('*',2,3),
    ('6',3,0),('7',3,1),('8',3,2),('-',3,3),
    ('9',4,0),('.',4,1),('+',4,2)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, bg='gray', fg='white', font=("Arial", 12, "bold"), command=lambda t=text:button_click(t))
    button.grid(row=row, column=col)

clear_button = tk.Button(root, text="clear", padx=10, pady=20, bg='skyblue', fg='white', font=("Arial", 10, "bold"), command=lambda: entry.delete(0,tk.END))
clear_button.grid(row=4, column=3, columnspan=1)

delete_button = tk.Button(root, text="Del", padx=40, pady=10, bg='skyblue', fg='white', font=("Arial", 12, "bold"), command=lambda: entry.delete(len(entry.get())-1))
delete_button.grid(row=5, column=0, columnspan=3)

equal_button = tk.Button(root, text="=", padx=40, pady=10, bg='orange', fg='white', font=("Arial", 12, "bold"),command=evaluate)
equal_button.grid(row=5, column=2, columnspan=3)

root.mainloop()
