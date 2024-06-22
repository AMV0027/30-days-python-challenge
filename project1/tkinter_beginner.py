import tkinter as tk

def button_click():
    label.config(text="Button Clicked !")

def show_entry_text():
    text = entry.get()
    label1.config(text="You entered : " + text)

def option1():
    label2.config(text="Option 1 Selected")

def option2():
    label2.config(text="Option 2 Selected")

# Create the main application window
window = tk.Tk()
window.title("My First Tkinter App")

#label creation
label = tk.Label(window,text="My First Tkinter")
label.pack()
name = tk.Label(window, text="Arunmozhi Varman" )
name.pack()

#button creation
button = tk.Button(window,text="Click me", command=button_click)
button.pack()

#input entry and button creation
entry = tk.Entry(window)
entry.pack()
button1 = tk.Button(window,text="Show text", command=show_entry_text)
button1.pack()
label1 = tk.Label(window,text="")
label1.pack()

#text creation

text = tk.Text(window)
text.pack()
text.insert(tk.END, "Hello everyone this is my first \nTinker cad project")

#check butotn
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
check1 = tk.Checkbutton(window,text="Opiton 1", variable=var1, command=option1)
check2 = tk.Checkbutton(window,text="option 2", variable=var2, command=option2)
check1.pack()
check2.pack()

label2 = tk.Label(window, text="")
label2.pack()
# Start the event loop
window.mainloop()
