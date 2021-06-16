import tkinter as tk
from tkinter import *
from Master import master


class rotor(master):
    def __init__(self):
        # creation of self variables
        self.rotor_a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                        "T", "U", "V", "W", "X", "Y", "Z"]
        self.rotor_b = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                        "T", "U", "V", "W", "X", "Y", "Z"]
        # creation of string variables
        self.var_a = StringVar()
        self.var_a.set(self.rotor_a[0])
        self.var_b = StringVar()
        self.var_b.set(self.rotor_b[0])

        super().__init__()

    def menu_extra(self):
        self.menu.title("RotorEncryption")
        tk.Button(self.wrapper2, text="decode", command=self.decode, width=self.b_width, height=self.b_height,
                  bd=self.b_b_width).pack(side=LEFT)
        Label(self.wrapper2, text="Rotor 1:").pack(side=LEFT)
        self.a_offset = tk.OptionMenu(self.wrapper2, self.var_a, *self.rotor_a)
        self.a_offset.configure(bd=self.b_b_width)
        self.a_offset.pack(side=LEFT)
        Label(self.wrapper2, text="Rotor 2:").pack(side=LEFT)
        self.b_offset = tk.OptionMenu(self.wrapper2, self.var_b, *self.rotor_b)
        self.b_offset.configure(bd=self.b_b_width)
        self.b_offset.pack(side=LEFT)
        tk.Button(self.wrapper2, text="encode", command=self.encode, width=self.b_width, height=self.b_height,
                  bd=self.b_b_width).pack(side=LEFT)

    def help(self):
        self.text_menu.insert(END,
                              """Help:
    this is the help text!""")

    def encode(self):
        pass

    def decode(self):
        pass
