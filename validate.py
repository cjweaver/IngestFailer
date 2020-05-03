import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

def validate_input(new_value):
    print(new_value)
    print(type(new_value))
    valid = (new_value .isdigit() and len(new_value) <= 5) or new_value == ''
    return valid

root = tk.Tk()

validate = root.register(validate_input)
for i in range(10):
    entry = tk.Entry(root, validate="key", validatecommand=(validate, "%P"))
    entry.pack(side="top", fill="x")

# Simple string entry popup
# name = askstring('Name', 'What is your name?')
# showinfo('Hello!', 'Hi, {}'.format(name))

root.mainloop()