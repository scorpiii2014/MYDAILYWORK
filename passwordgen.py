import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be greater than zero.")

        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        use_numbers = numbers_var.get()
        use_specials = specials_var.get()

        character_pool = ""
        if use_uppercase:
            character_pool += string.ascii_uppercase
        if use_lowercase:
            character_pool += string.ascii_lowercase
        if use_numbers:
            character_pool += string.digits
        if use_specials:
            character_pool += string.punctuation

        if not character_pool:
            messagebox.showerror("Error", "No character types selected.")
            return

        password = ''.join(random.choice(character_pool) for _ in range(length))
        password_display.delete(0, tk.END)
        password_display.insert(0, password)

    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")


# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_display.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()  # Now it stays in clipboard after window is closed
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")


# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="Password Generator", font=("Arial", 16))
title_label.pack(pady=10)

# Password Length
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Character Options
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
specials_var = tk.BooleanVar()

uppercase_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.pack()

lowercase_check = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var)
lowercase_check.pack()

numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_check.pack()

specials_check = tk.Checkbutton(root, text="Include Special Characters", variable=specials_var)
specials_check.pack()

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Password Display
password_display = tk.Entry(root, font=("Arial", 12), justify="center")
password_display.pack(pady=5)

# Copy Button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Run the GUI event loop
root.mainloop()
