import tkinter as tk
from cryptography.fernet import Fernet
from Master import master


class key(master):
    def __init__(self):
        # declaration of self variables
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
        super().__init__()

    def menu_extra(self):
        self.menu.title("Keys")
        # filling of frame 2
        tk.Button(self.frame2, text="Decode", command=self.decrypt, width=self.b_width, height=self.b_height).pack(
            side=tk.LEFT)
        tk.Label(self.frame2, text="Key:").pack(side=tk.LEFT)
        self.key_box = tk.Entry(self.frame2, width=50)
        self.key_box.pack(side=tk.LEFT)
        self.key_box.insert(tk.END, self.key)
        tk.Button(self.frame2, text="Encode", command=self.encrypt, width=self.b_width, height=self.b_height).pack(
            side=tk.RIGHT)

    def encrypt(self):
        encoded = self.fernet.encrypt(self.get_text().encode("utf-8"))
        print(encoded)

    def decrypt(self):
        text = self.fernet.decrypt(self.get_text().encode("utf-8"))
        print(text)


key()
