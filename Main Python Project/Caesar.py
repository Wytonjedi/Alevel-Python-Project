from tkinter import *
import random
from Master import master


class caesar(master):
    def __init__(self):
        self.type = "Caesar"
        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                        "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        super().__init__()

    def type(self):
        self.type = "caesar"

    def menu_extra(self):
        # setting window title
        self.menu.title("Caesar")

        # filling of Wrapper2
        Button(self.wrapper2, text="Decode", command=self.decrypt, width=self.b_width, height=self.b_height,
               bd=self.b_b_width).pack(side=LEFT)
        Label(self.wrapper2, text="Shift:").pack(side=LEFT)
        self.key = StringVar()
        self.key.set(self.numbers[random.randint(0, len(self.numbers))])
        self.shift_drop = OptionMenu(self.wrapper2, self.key, *self.numbers)
        self.shift_drop.configure(width=10, bd=self.b_b_width)
        self.shift_drop.pack(side=LEFT)
        Button(self.wrapper2, text="Encode", command=self.encrypt, width=self.b_width, height=self.b_height,
               bd=self.b_b_width).pack(side=RIGHT)

    def help(self):
        self.text_menu.insert(END,
                              """Help:
    this is the help text!""")

    def get_shift(self, count):
        shift = self.key.get()
        return int(shift)

    def shift(self, char, shift):
        for i in range(len(self.letters)):
            if self.letters[i] == char:
                j = i + shift
                if j > (len(self.letters) - 1):
                    j = j - len(self.letters)
                return self.letters[j]

    def encrypt(self):
        text = self.get_text()
        count = 0
        encoded = ""
        for i in range(len(text) - 1):
            run = False
            for j in range(len(self.letters)):
                if text[i].upper() == self.letters[j]:
                    encoded = encoded + self.shift(text[i], self.get_shift(count)).upper()
                    count += 1
                    run = True
            if not run:
                encoded = encoded + text[i]
        self.encoded_menu.delete("1.0", END)
        self.encoded_menu.insert(END, encoded)

    def decrypt(self):
        encoded = self.encoded_menu.get("1.0", END).upper()
        count = 0

        text = ""
        for i in range(len(encoded) - 1):
            decrypt = False
            for j in range(len(self.letters)):
                if encoded[i] == self.letters[j]:
                    text += self.shift(encoded[i], (len(self.letters) - self.get_shift(count)))
                    count += 1
                    decrypt = True
            if not decrypt:
                text += encoded[i]
        self.text_menu.delete("1.0", END)
        self.text_menu.insert(END, text)
