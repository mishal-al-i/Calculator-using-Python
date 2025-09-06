import tkinter as tk
import math

# Function to handle button press
def on_click(value):
    current = display_var.get()
    if value == 'C':
        display_var.set('')
    elif value == '=':
        try:
            display_var.set(str(eval(current)))
        except Exception:
            display_var.set('Error')
    elif value == '%':
        try:
            display_var.set(str(eval(current) / 100))
        except Exception:
            display_var.set('Error')
    elif value == '√':
        try:
            display_var.set(str(math.sqrt(float(current))))
        except Exception:
            display_var.set('Error')
    else:
        display_var.set(current + value)

# Set up main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")  # Bigger screen
root.resizable(False, False)

# Display variable and entry
display_var = tk.StringVar()
entry = tk.Entry(root, textvariable=display_var, font=("Arial", 30), bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=20, padx=10, ipady=10)

# Button layout
buttons = [
    ('C',1,0), ('√',1,1), ('%',1,2), ('/',1,3),
    ('7',2,0), ('8',2,1), ('9',2,2), ('*',2,3),
    ('4',3,0), ('5',3,1), ('6',3,2), ('-',3,3),
    ('1',4,0), ('2',4,1), ('3',4,2), ('+',4,3),
    ('0',5,0), ('.',5,1), ('=',5,2),
]

# Create buttons
for (text, row, col) in buttons:
    action = lambda t=text: on_click(t)
    tk.Button(root, text=text, width=5, height=2, font=("Arial", 24), command=action)\
      .grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Span the '=' over two columns for better visibility
tk.Button(root, text='=', width=5, height=2, font=("Arial", 24), command=lambda: on_click('='))\
   .grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

# Make columns expand equally
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
