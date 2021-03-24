import tkinter as tk
import random
from Caesar import caesar

class vigenere(caesar):
    def __init__(self):
        self.type = "Vigenere"
        super().__init__()

    def menu_extra(self):
        self.menu.title("Vigenere")
        tk.Button(self.frame2, text="Decode", command=self.decrypt, width=self.b_width, height=self.b_height).pack(
            side=tk.LEFT)
        self.key = tk.Entry(self.frame2)
        self.key.pack(side=tk.LEFT)
        tk.Button(self.frame2, text="Encode", command=self.encrypt, width=self.b_width, height=self.b_height).pack(
            side=tk.RIGHT)

    def get_shift(self, i):
        key = self.key.get().upper()
        if i > len(key) - 1:
            i = i % len(key)
        for j in range(0, len(self.letters) - 1):
            if key[i] == self.letters[j]:
                return j


