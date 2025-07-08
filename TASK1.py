import tkinter as tk
# Create main window
root = tk.Tk()
root.title("T-Do List")
root.geometry("300x400")
root.configure(bg="lightblue")
# Task list
tasks = []
# Add task function
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
# Delete selected task
def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
        tasks.pop(selected[0])
# Entry box
entry = tk.Entry(root, width=25 , bg="white", fg="black", font=("Arial", 12))
entry.pack(pady=10)
# Button
add_btn = tk.Button(root, text="Add Task",bg="green", fg="white", command=add_task)
add_btn.pack()
delete_btn = tk.Button(root, text="Delete Task", bg="red", fg="white",command=delete_task)
delete_btn.pack(pady=5)
# Task display
listbox = tk.Listbox(root, width=30, height=10, bg="lightyellow", fg="magenta", font=("Arial", 11))
listbox.pack(pady=10)
# Start GUI loop
root.mainloop()
