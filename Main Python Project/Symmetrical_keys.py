from tkinter import *
from cryptography.fernet import Fernet
from Master import master


class key_sym(master):
    def __init__(self):
        self.type = "Key_Sym"
        # declaration of self variables
        self.type = "Symmetrical Keys"
        self.Sym_key = Fernet.generate_key()
        self.token = Fernet(self.Sym_key)
        super().__init__()

    def menu_extra(self):
        # setting of menu title
        self.menu.title("Symmetrical Keys")

        # filling of wrapper2
        Button(self.wrapper2, text="Decode", command=self.decrypt, width=self.b_width, height=self.b_height,
               bd=self.b_b_width).pack(side=LEFT)
        Label(self.wrapper2, text="Key:").pack(side=LEFT)
        self.key = Entry(self.wrapper2, width=50)
        self.key.pack(side=LEFT)
        self.key.insert(END, self.Sym_key)
        Button(self.wrapper2, text="Encode", command=self.encrypt, width=self.b_width, height=self.b_height,
               bd=self.b_b_width).pack(side=RIGHT)

    def help(self):
        self.text_menu.insert(END,
                              """Help:
    this is the help text!""")

    def encrypt(self):
        encoded = self.token.encrypt(self.get_text().encode("utf-8"))
        self.encoded_menu.delete("1.0", END)
        self.encoded_menu.insert(END, encoded)

    def decrypt(self):  # need to use same token as when encrypted? save token as well?
        text = self.token.decrypt(self.get_encoded_text().encode("utf-8"))
        self.text_menu.delete("1.0", END)
        self.text_menu.insert(END, text)
