# DOES NOT WORK!!

import rsa
from tkinter import *
from Symmetrical_keys import key_sym
from Master import master


class key_asym(master):
    def __init__(self):
        # decleration of self Variables
        self.type = "Asymmetrical Keys"
        self.public_key, self.private_key = rsa.newkeys(512)
        super().__init__()

    def menu_extra(self):
        self.menu.title("Asymmetrical keys")

        # filling of wrapper2
        Button(self.wrapper2, text="Decode", command=self.decrypt, width=self.b_width, height=self.b_height,
               bd=self.b_b_width).pack(side=LEFT)
        Label(self.wrapper2, text=" Public Key:").pack(side=LEFT)
        self.key = Entry(self.wrapper2, width=50)
        self.key.pack(side=LEFT)
        self.key.insert(END, self.public_key)
        Button(self.wrapper2, text="Encode", command=self.encrypt, width=self.b_width, height=self.b_height,
               bd=self.b_b_width).pack(side=RIGHT)

    def get_keys(self):  # NOT CURRENTLY IN USE!
        try:
            f = open("keys.txt", "rb")
            private, public = f.readlines()
        except:
            private, public = rsa.newkeys(16)
            f = open("keys.txt", "wb")
            f.writelines(private)
            f.writelines(public)
        return private, public

    def help(self):
        self.text_menu.insert(END,
                              """Help:
    this is the help text!""")

    def encrypt(self):
        text = bytes(self.get_text().encode("utf-8"))
        try:
            encoded = rsa.encrypt(text, self.public_key)
        except:
            self.encoded_menu.delete("1.0", END)
            self.encoded_menu.insert(END, "ERROR: Message too long")
        else:
            self.encoded_menu.delete("1.0", END)
            self.encoded_menu.insert(END, encoded)


    def decrypt(self):
        encoded = self.get_encoded_text()
        text = rsa.decrypt(encoded, self.private_key).decode()
        self.text_menu.delete("1.0", END)
        self.text_menu.insert(END, text)
