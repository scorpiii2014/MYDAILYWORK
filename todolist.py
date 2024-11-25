import tkinter as tk
from tkinter import messagebox

def add_task():
    task_text = task_entry.get()
    if task_text:
        # Create a frame for the task with a border
        task_frame = tk.Frame(task_list_frame, bg="#d9ead3", bd=2, relief="ridge", padx=5, pady=5)
        task_frame.pack(anchor='w', fill='x', pady=5, padx=10)

        # Create a checkbox (Checkbutton) for the task
        task_var = tk.IntVar()  # Tracks if the checkbox is checked
        task_checkbox = tk.Checkbutton(task_frame, text=task_text, variable=task_var,
                                       font=("Arial", 12), bg="#d9ead3", anchor='w')
        task_checkbox.pack(side='left', padx=5, fill='x', expand=True)

        # Add a delete button next to each task
        delete_button = tk.Button(task_frame, text="❌", command=lambda: delete_task(task_frame),
                                  bg="#f4cccc", fg="black", bd=0, font=("Arial", 10))
        delete_button.pack(side='right', padx=5)

        # Clear the input field after adding
        task_entry.delete(0, tk.END)

        # Show a success message
        messagebox.showinfo("Success", "Task added successfully!")
    else:
        messagebox.showwarning("Warning", "Please enter a task!")


def delete_task(task_frame):
    # Destroy the task frame (removes the task from the list)
    task_frame.destroy()


def clear_tasks():
    # Destroy all task frames inside the task list frame
    for widget in task_list_frame.winfo_children():
        widget.destroy()


# Set up the main application window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.configure(bg='#f0f0f0')

# Add input field for tasks
task_entry = tk.Entry(root, width=35, font=("Arial", 14))
task_entry.pack(pady=20)

# Add buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", width=12, command=add_task, bg="#b6d7a8", font=("Arial", 10))
add_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(button_frame, text="Clear All", width=12, command=clear_tasks, bg="#f4cccc",
                         font=("Arial", 10))
clear_button.grid(row=0, column=1, padx=5)

# Task list display area 
task_list_frame = tk.Frame(root, bg="#f0f0f0")
task_list_frame.pack(pady=10, fill='both', expand=True)

# Run the application
root.mainloop()
