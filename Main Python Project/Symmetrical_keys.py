import tkinter as tk
from cryptography.fernet import Fernet
import sys

sys.path.append(".")
from Master import master


class Key(master):
    def __init__(self):
        # declaration of self variables
        self.key = Fernet.generate_key()
        super().__init__()

    def menu_extra(self):
        self.window.title("Keys")
        # filling of frame 2
        tk.Button(self.frame2, text="Decode", command=self.decrypt).pack(side=tk.LEFT)
        self.key_box = tk.Entry(self.frame2, width=int(self.width - 2 * (self.width / 6)))
        self.key_box.pack(side=tk.LEFT)
        self.key_box.insert(tk.END, self.key)
        tk.Button(self.frame2, text="Encode", command=self.encrypt).pack(side=tk.RIGHT)

    def encrypt(self):
        key = Fernet(self.key)
        encoded = key.encrypt(self.get_text().encode("utf-8"))
        print(encoded)

    def decrypt(self):
        key = Fernet(self.key)
        text = key.decrypt(self.get_text().encode("utf-8"))
        print(text)


Key()
