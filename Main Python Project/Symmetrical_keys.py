from tkinter import *
from cryptography.fernet import Fernet
from Master import master


class key(master):
    def __init__(self):
        # declaration of self variables
        self.key = Fernet.generate_key()
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
        token = Fernet(self.key)
        encoded = token.encrypt(self.get_text().encode("utf-8"))
        self.encoded_menu.delete("1.0", END)
        self.encoded_menu.insert(END, encoded)

    def decrypt(self):
        token = Fernet(self.key)
        text = token.decrypt(self.get_encoded_text().encode("utf-8"))
        self.text_menu.delete("1.0", END)
        self.text_menu.insert(END, text)
