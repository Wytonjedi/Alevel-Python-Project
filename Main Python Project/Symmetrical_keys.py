from tkinter import *
from cryptography.fernet import Fernet
from Master import master


class key(master):
    def __init__(self):
        # declaration of self variables
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
        super().__init__()

    def menu_extra(self):
        # setting of menu title
        self.menu.title("Keys")

        # filling of wrapper2
        Button(self.wrapper2, text="Decode", command=self.decrypt, width=self.b_width, height=self.b_height,
               bd=self.b_b_width).pack(side=LEFT)
        Label(self.wrapper2, text="Key:").pack(side=LEFT)
        self.key_box = Entry(self.wrapper2, width=50)
        self.key_box.pack(side=LEFT)
        self.key_box.insert(END, self.key)
        Button(self.wrapper2, text="Encode", command=self.encrypt, width=self.b_width, height=self.b_height,
               bd=self.b_b_width).pack(side=RIGHT)

    def encrypt(self):
        encoded = self.fernet.encrypt(self.get_text().encode("utf-8"))
        print(encoded)

    def decrypt(self):
        text = self.fernet.decrypt(self.get_text().encode("utf-8"))
        print(text)
