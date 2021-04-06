from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Caesar import caesar
from Vigenere import vigenere
from Symmetrical_keys import key
from Rotor_encryption import rotor




class menu:
    def __init__(self):
        self.root = tk.Tk()

        self.option = ""

        self.wrapper1 = LabelFrame(self.root, text="Encode options")
        self.wrapper2 = LabelFrame(self.root, text="Description")
        self.wrapper3 = LabelFrame(self.root, text="Options")

        # filling wrapper1
        Button(self.wrapper1, text="caesar", width=15, height=1, bd=4).pack()
        Button(self.wrapper1, text="vigenere", width=15, height=1, bd=4).pack()
        Button(self.wrapper1, text="symmetrical keys", width=15, height=1, bd=4).pack()
        Button(self.wrapper1, text="Rotor encryption", width=15, height=1, bd=4).pack()

        # filling wrapper2
        self.description = tk.Text(self.wrapper2, state="disabled", width=75, height=15)
        self.description.pack()

        # filling wrapper3
        tk.Button(self.wrapper3, text="Exit", width=15, height=1, bd=4, fg="red"
                  ).pack(side=tk.LEFT)
        tk.Button(self.wrapper3, text="Enter", width=15, height=1, bd=4).pack(side=tk.RIGHT)

        # putting wrappers onto window
        self.wrapper1.grid(row=0, column=0, sticky=N+S)
        self.wrapper2.grid(row=0, column=1)
        self.wrapper3.grid(row=1, columnspan=2, sticky=E+W)

        self.root.title("Main Menu")
        self.root.mainloop()


menu()