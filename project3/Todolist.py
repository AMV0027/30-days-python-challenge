import tkinter as tk
from tkinter import messagebox, END

task_list = []
counter = 1

def inputError():
    if enterTaskFeild.get() == "":
        messagebox.showerror("Error", "Please enter a task")
        return 0
    return 1

def clear_taskNumberField():
    taskNumberFeild.delete(1.0, END)

def clear_taskField():
    enterTaskFeild.delete(0, END)

def insertTask():
    global counter
    value = inputError()
    if value == 0:
        return
    content = enterTaskFeild.get() + "\n"
    task_list.append(content)
    textArea.insert('end -1 chars', "[" + str(counter) + "]" + content)
    counter += 1
    clear_taskField()

def delete_task():
    global counter
    if len(task_list) == 0:
        messagebox.showerror("Error", "No task to delete")
        return
    number = taskNumberFeild.get(1.0, END)
    if number == "\n":
        messagebox.showerror("Error", "Please enter a number")
        return
    else:
        task_no = int(number)
    clear_taskNumberField()
    task_list.pop(task_no - 1)
    counter -= 1
    textArea.delete(1.0, END)
    for i in range(len(task_list)):
        textArea.insert('end -1 chars', "[" + str(i + 1) + "]" + task_list[i])

def exit_app():
    gui.destroy()

if __name__ == "__main__":
    gui = tk.Tk()
    gui.configure(background="grey")
    gui.title("Todo app")
    gui.geometry("350x300")

    enterTask = tk.Label(gui, text="Enter task", bg="black", fg="white")
    enterTaskFeild = tk.Entry(gui)

    submit = tk.Button(gui, text="Submit", bg="black", fg="white", command=insertTask)

    textArea = tk.Text(gui, height=5, width=25)

    taskNumber = tk.Label(gui, text="Delete Task Number", bg="skyblue")
    taskNumberFeild = tk.Text(gui, height=1, width=2)

    delete_btn = tk.Button(gui, text="Delete", fg="white", bg="red", command=delete_task)

    Exit = tk.Button(gui, text="Exit", fg="white", bg="black", command=exit_app)

    enterTask.grid(row=0, column=1)
    enterTaskFeild.grid(row=0, column=2, ipadx=50)
    submit.grid(row=0, column=3)
    textArea.grid(row=3, column=2, padx=10)
    taskNumber.grid(row=4, column=2)
    taskNumberFeild.grid(row=5, column=2)
    delete_btn.grid(row=6, column=2)
    Exit.grid(row=7, column=2)

    gui.mainloop()
