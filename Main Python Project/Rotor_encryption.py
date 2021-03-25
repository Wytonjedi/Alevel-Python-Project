import tkinter as tk
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
        tk.Button(self.frame2, text="decode", command=self.decode).pack()
        self.a_offset = tk.OptionMenu(self.frame2, self.a_var, *self.alpha)
        self.a_offset.pack()
        self.b_offset = tk.OptionMenu(self.frame2, self.b_var, *self.bravo)
        self.b_offset.pack()
        tk.Button(self.frame2, text="encode", command=self.encode).pack()

    def get_offset(self):
        self.offset[0] = self.a_var.get()
        self.offset[1] = self.b_var.get()

    def encode(self):
        pass

    def decode(self):
        pass
