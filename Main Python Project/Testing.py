from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Caesar import caesar
from Vigenere import vigenere
from Symmetrical_keys import key
from Rotor_encryption import rotor

root = tk.Tk()

wrapper1 = LabelFrame(root, text="Encode options")
wrapper2 = LabelFrame(root, text="Description")
wrapper3 = LabelFrame(root, text="Options")

# filling wrapper1
Button(wrapper1, text="caesar", width=15, height=1, bd=4).pack()
Button(wrapper1, text="vigenere", width=15, height=1, bd=4).pack()
Button(wrapper1, text="symmetrical keys", width=15, height=1, bd=4).pack()
Button(wrapper1, text="Rotor encryption", width=15, height=1, bd=4).pack()

# filling wrapper2
description = tk.Text(wrapper2, width=75, height=15)
description.pack()

# filling wrapper3
tk.Button(wrapper3, text="Exit", width=15, height=1, bd=4, fg="red"
          ).pack(side=tk.LEFT)
tk.Button(wrapper3, text="Enter", width=15, height=1, bd=4).pack(side=tk.RIGHT)

# putting wrappers onto window
wrapper1.grid(row=0, column=0)
wrapper2.grid(row=0, column=1)
wrapper3.grid(row=1, columnspan=2, ipadx="200")

root.title("Main Menu")
root.mainloop()
