import tkinter as tk
from tkinter import *
from Master import master


class rotor(master):
    def __init__(self):
        # creation of string variables
        self.alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                      "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.bravo = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                      "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.a_var = tk.StringVar()
        self.a_var.set(self.alpha[0])
        self.b_var = tk.StringVar()
        self.b_var.set(self.bravo[0])

        super().__init__()

        self.offset = []
        self.plugs = []

    def menu_extra(self):
        self.menu.title("RotorEncryption")
        tk.Button(self.wrapper2, text="decode", command=self.decode, width=self.b_width, height=self.b_height,
                  bd=self.b_b_width).pack(side=LEFT)
        Label(self.wrapper2, text="Rotor 1:").pack(side=LEFT)
        self.a_offset = tk.OptionMenu(self.wrapper2, self.a_var, *self.alpha)
        self.a_offset.configure(bd=self.b_b_width)
        self.a_offset.pack(side=LEFT)
        Label(self.wrapper2, text="Rotor 2:").pack(side=LEFT)
        self.b_offset = tk.OptionMenu(self.wrapper2, self.b_var, *self.bravo)
        self.b_offset.configure(bd=self.b_b_width)
        self.b_offset.pack(side=LEFT)
        tk.Button(self.wrapper2, text="encode", command=self.encode, width=self.b_width, height=self.b_height,
                  bd=self.b_b_width).pack(side=LEFT)

    def help(self):
        self.text_menu.insert(END,
                              """Help:
    this is the help text!""")

    def get_offset(self):
        self.offset[0] = self.a_var.get()
        self.offset[1] = self.b_var.get()

    def encode(self):
        pass

    def decode(self):
        pass
