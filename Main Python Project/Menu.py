from tkinter import *
import tkinter as tk
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
        Button(self.wrapper1, text="caesar", command=self.choose_caesar, width=15, height=1, bd=4).pack()
        Button(self.wrapper1, text="vigenere", command=self.choose_vigenere, width=15, height=1, bd=4).pack()
        Button(self.wrapper1, text="symmetrical keys", command=self.choose_key, width=15, height=1, bd=4).pack()
        Button(self.wrapper1, text="Rotor encryption", command=self.choose_rotor, width=15, height=1, bd=4).pack()

        # filling wrapper2
        self.description = tk.Text(self.wrapper2, state="disabled", width=75, height=15)
        self.description.pack()

        # filling wrapper3
        tk.Button(self.wrapper3, text="Exit", command=self.root.destroy, width=15, height=1, bd=4, fg="red"
                  ).pack(side=tk.LEFT)
        tk.Button(self.wrapper3, text="Enter", command=self.enter, width=15, height=1, bd=4).pack(side=tk.RIGHT)

        # putting wrappers onto window
        self.wrapper1.grid(row=0, column=0, sticky=N+S)
        self.wrapper2.grid(row=0, column=1)
        self.wrapper3.grid(row=1, columnspan=2, sticky=E+W)

        self.root.title("Main Menu")
        self.root.mainloop()

    def choose_caesar(self):
        self.description.configure(state="normal")
        self.description.delete("1.0", tk.END)
        self.description.insert(tk.END,
"""Caesar:

this is one of the first cyphers ever created""")
        self.description.configure(state="disabled")
        self.option = "c"

    def choose_vigenere(self):
        self.description.configure(state="normal")
        self.description.delete("1.0", tk.END)
        self.description.insert(tk.END,
"""Vigenere:

This was developed from the Caesar cypher using a key instead of 
a stationary shift""")
        self.description.configure(state="disabled")
        self.option = "v"

    def choose_key(self):
        self.description.configure(state="normal")
        self.description.delete("1.0", tk.END)
        self.description.insert(tk.END,
"""Symmetrical Keys:

this is the most commonly used encryption methods used to day """)
        self.description.configure(state="disabled")
        self.option = "k"

    def choose_rotor(self):
        self.description.configure(state="normal")
        self.description.delete("1.0", tk.END)
        self.description.insert(tk.END,
"""Rotor:

this is a watered down version of the enigma machine used by the NAZIs""")
        self.description.configure(state="disabled")

        self.option = "r"

    def back(self):
        self.description.configure(state="normal")
        self.description.delete("1.0", tk.END)
        self.description.configure(state="disabled")

        self.option = ""

    def enter(self):
        if self.option == "c":
            caesar()
        elif self.option == "v":
            vigenere()
        elif self.option == "k":
            key()
        elif self.option == "r":
            rotor()
        else:
            print("Not option selected")


menu()