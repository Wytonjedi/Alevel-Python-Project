import tkinter as tk
import random
from Master import master


class caesar(master):
    def __init__(self):
        self.type = "caesar"
        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                        "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        super().__init__()

    def menu_extra(self):
        self.menu.title("Caesar")
        # filling of frame 2
        tk.Button(self.frame2, text="Decode", command=self.decrypt, width=self.b_width, height=self.b_height).pack(
            side=tk.LEFT)
        self.key = tk.StringVar()
        self.key.set(self.numbers[random.randint(0, len(self.numbers))])
        self.shift_drop = tk.OptionMenu(self.frame2, self.key, *self.numbers)
        self.shift_drop.configure(width=10)
        self.shift_drop.pack(side=tk.LEFT)
        tk.Button(self.frame2, text="Encode", command=self.encrypt, width=self.b_width, height=self.b_height).pack(
            side=tk.RIGHT)

    def get_shift(self, i):
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
        run = bool()
        for i in range(len(text) - 1):
            run = False
            for j in range(len(self.letters)):
                if text[i].upper() == self.letters[j]:
                    encoded = encoded + self.shift(text[i], self.get_shift(count)).upper()
                    count += 1
                    run = True
            if not(run):
                encoded = encoded + text[i]
        self.encoded_menu.delete("1.0", tk.END)
        self.encoded_menu.insert(tk.END, encoded)

    def decrypt(self):
        encoded = self.encoded_menu.get("1.0", tk.END)
        for i in range(1, len(self.numbers)):
            text = ""
            for j in range(len(encoded)):
                text = text + self.shift(encoded[j], i)
            print(text)

caesar()