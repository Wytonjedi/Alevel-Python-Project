import smtplib
import ssl
import tkinter as tk
import random


class master:
    def __init__(self):
        # set height and widths
        # text boxs
        self.t_width = 75
        self.t_height = 15
        # Buttons
        self.b_width = 15
        self.b_height = 1

        # email vars
        self.port = 587
        self.smtp_server = "smtp.gmail.com"
        self.master_email = "mypythonprojects101@gmail.com"
        self.master_password = "htcgfnmoxctenucn"

        # creation of window
        self.window = tk.Tk()

        # creation of frames
        self.frame1 = tk.Frame(self.window)
        self.frame2 = tk.Frame(self.window)
        self.frame3 = tk.Frame(self.window)
        self.frame4 = tk.Frame(self.window)

        # filling of frame 1
        self.text_menu = tk.Text(self.frame1, width=self.t_width, height=self.t_height)
        self.text_menu.pack()

        self.menu_extra()

        # filling of frame 3
        self.encoded_menu = tk.Text(self.frame3, width=self.t_width, height=self.t_height)
        self.encoded_menu.pack()

        # filling of frame 4
        tk.Button(self.frame4, text="Back", command=self.window.destroy, width=self.b_width, height=self.b_height).pack(
            side=tk.LEFT)
        tk.Button(self.frame4, text="Email to friends", command=self.email, width=self.b_width,
                  height=self.b_height).pack(side=tk.LEFT)
        tk.Button(self.frame4, text="Save to file", width=self.b_width, height=self.b_height).pack(side=tk.RIGHT)

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
        self.menu = tk.Tk()
        self.frame1 = tk.Frame(self.menu)
        self.frame2 = tk.Frame(self.menu)
        self.frame3 = tk.Frame(self.menu)

        # filling frame 1
        self.receiver = tk.Entry(self.frame1)
        self.receiver.pack()

        # filling frame 2
        self.message = tk.Text(self.frame2)
        self.message.insert(tk.END, """
Method: {} 
Encoded Text: {}
Key: {}

Look at this!""".format(self.type, self.encoded_menu.get("1.0", tk.END), self.key.get()))
        self.message.pack()

        # filling frame 3
        tk.Button(self.frame3, text="cancel", command=self.menu.destroy).pack(side=tk.LEFT)
        tk.Button(self.frame3, text="send", command=self.send).pack(side=tk.RIGHT)

        # packing frames
        self.frame1.pack(side=tk.TOP)
        self.frame2.pack()
        self.frame3.pack(side=tk.BOTTOM)
        self.menu.mainloop()

    def send(self):
        context = ssl.create_default_context()
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.starttls(context=context)
        server.login(self.master_email, self.master_password)
        server.sendmail(self.master_email, self.receiver.get(), self.message.get(tk.END))

    def save_to_file(self):
        pass


class caesar(master):
    def __init__(self):
        self.type = "caesar"
        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                        "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        super().__init__()

    def menu_extra(self):
        # filling of frame 2
        tk.Button(self.frame2, text="Decode", command=self.decrypt, width=self.b_width, height=self.b_height).pack(
            side=tk.LEFT)
        self.key = tk.StringVar()
        self.key.set(self.numbers[random.randint(0, len(self.numbers))])
        self.shift_drop = tk.OptionMenu(self.frame2, self.key, *self.numbers)
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
        for i in range(len(text) - 1):
            if text[i] == " ":
                encoded = encoded + " "
            else:
                encoded = encoded + self.shift(text[i], self.get_shift(count))
                count += 1
        self.encoded_menu.delete("1.0", tk.END)
        self.encoded_menu.insert(tk.END, encoded)

    def decrypt(self):
        encoded = self.encoded_menu.get("1.0", tk.END)
        for i in range(1, len(self.numbers)):
            text = ""
            for j in range(len(encoded)):
                text = text + self.shift(encoded[j], i)
            print(text)


class vigenere(caesar):
    def __init__(self):
        self.type = "Vigenere"
        super().__init__()

    def menu_extra(self):
        tk.Button(self.frame2, text="Decode", command=self.decrypt, width=self.b_width, height=self.b_height).pack(
            side=tk.LEFT)
        self.key = tk.Entry(self.frame2)
        self.key.pack(side=tk.LEFT)
        tk.Button(self.frame2, text="Encode", command=self.encrypt, width=self.b_width, height=self.b_height).pack(
            side=tk.RIGHT)

    def get_shift(self, i):
        key = self.key.get().upper()
        if i > len(key) - 1:
            i = i % len(key)
        for j in range(0, len(self.letters) - 1):
            if key[i] == self.letters[j]:
                return j


caesar()
