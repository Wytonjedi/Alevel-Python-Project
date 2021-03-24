import tkinter as tk
from cryptography.fernet import Fernet

class master:
    def __init__(self):
        self.width = 75
        self.height = 15

        # creation of window
        self.window = tk.Tk()

        # creation of frames
        self.frame1 = tk.Frame(self.window)
        self.frame2 = tk.Frame(self.window)
        self.frame3 = tk.Frame(self.window)
        self.frame4 = tk.Frame(self.window)

        # filling of frame 1
        self.text_menu = tk.Text(self.frame1, width=self.width, height=self.height)
        self.text_menu.pack()

        self.menu_extra()

        # filling of frame 3
        self.encoded_menu = tk.Text(self.frame3, width=self.width, height=self.height)
        self.encoded_menu.pack()

        # filling of frame 4
        tk.Button(self.frame4, text="Email to friends").pack(side=tk.LEFT)
        tk.Button(self.frame4, text="Save to file").pack(side=tk.RIGHT)

        # packing frames
        self.frame1.pack(side=tk.TOP)
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack(side=tk.BOTTOM)
        self.window.mainloop()

    def get_text(self):
        text = self.text_menu.get("1.0", tk.END)
        return text.upper()

    def email(self):
        pass

    def save_to_file(self):
        pass


class Key(master):
    def __init__(self):
        # declaration of self variables
        self.key = Fernet.generate_key()
        super().__init__()

    def menu_extra(self):
        self.window.title("Keys")
        # filling of frame 2
        tk.Button(self.frame2, text="Decode", command=self.decrypt).pack(side=tk.LEFT)
        self.key_box = tk.Entry(self.frame2, width=int(self.width-2*(self.width/6)))
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
