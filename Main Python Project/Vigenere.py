from tkinter import *
from Caesar import caesar


class vigenere(caesar):
    def __init__(self):
        self.type = "Vigenere"
        super().__init__()

    def menu_extra(self):
        # setting menu title
        self.menu.title("Vigenere")

        # filling of wrapper2
        Button(self.wrapper2, text="Decode", command=self.decrypt, width=self.b_width, height=self.b_height,
               bd=self.b_b_width).pack(side=LEFT)
        Label(self.wrapper2, text="Key:").pack(side=LEFT)
        self.key = Entry(self.wrapper2)
        self.key.pack(side=LEFT)
        Button(self.wrapper2, text="Encode", command=self.encrypt, width=self.b_width, height=self.b_height,
               bd=self.b_b_width).pack(side=RIGHT)

    def help(self):
        self.text_menu.insert(END,
                              """Help:
    this is the help text!""")

    def get_shift(self, i):
        key = self.key.get().upper()
        if i > len(key) - 1:
            i = i % len(key)
        for j in range(0, len(self.letters) - 1):
            if key[i] == self.letters[j]:
                return j
