import tkinter as tk
from tkinter import *
import smtplib
import ssl
import os


class master:
    def __init__(self):
        # set height and widths
        # text boxes
        self.t_width = 75
        self.t_height = 15
        # Buttons
        self.b_width = 15
        self.b_height = 1
        self.b_b_width = 4

        # email vars
        self.port = 587
        self.smtp_server = "smtp.gmail.com"
        self.master_email = "mypythonprojects101@gmail.com"
        self.master_password = os.environ.get("EMAIL_TOKEN")

        # creation of window
        self.menu = Toplevel()

        # creation of frames
        self.wrapper1 = LabelFrame(self.menu, text="Plain Text")
        self.wrapper2 = LabelFrame(self.menu, text="Encoding Method")
        self.wrapper3 = LabelFrame(self.menu, text="Encoded Text")
        self.wrapper4 = LabelFrame(self.menu, text="Options")

        # filling of wrapper1
        self.text_menu = Text(self.wrapper1, width=self.t_width, height=self.t_height)
        self.text_menu.pack()

        # filling of wrapper2 from subclass
        self.menu_extra()

        # filling of wrapper3
        self.encoded_menu = Text(self.wrapper3, width=self.t_width, height=self.t_height)
        self.encoded_menu.pack()

        # filling of frame 4
        Button(self.wrapper4, text="Back", command=self.menu.destroy, width=self.b_width, height=self.b_height,
               bd=self.b_b_width).pack(
            side=LEFT)
        Button(self.wrapper4, text="Help", width=self.b_width, height=self.b_height,
               bd=self.b_b_width).pack(
            side=LEFT)
        Button(self.wrapper4, text="Email to friends", command=self.email, width=self.b_width,
               height=self.b_height, bd=self.b_b_width).pack(side=RIGHT)
        Button(self.wrapper4, text="Save to file", command=self.save_to_file, width=self.b_width,
               height=self.b_height, bd=self.b_b_width).pack(side=RIGHT)

        # packing frames
        self.wrapper1.pack(side=TOP, fill="x")
        self.wrapper2.pack()
        self.wrapper3.pack(fill="x")
        self.wrapper4.pack(side=BOTTOM, fill="x")
        self.menu.mainloop()

    def get_text(self):
        text = self.text_menu.get("1.0", tk.END)
        return text.upper()

    def get_encoded_text(self):
        encrypted = self.encoded_menu.get("1.0", END)
        return encrypted.upper()

    def email(self):
        self.menu = tk.Tk()
        self.frame1 = tk.Frame(self.menu)
        self.frame2 = tk.Frame(self.menu)
        self.frame3 = tk.Frame(self.menu)

        # filling frame 1
        tk.Label(self.frame1, text="Enter Email:").pack(side=tk.LEFT)
        self.receiver = tk.Entry(self.frame1)
        self.receiver.pack(side=tk.RIGHT)

        # filling frame 2
        self.message = tk.Text(self.frame2)
        self.message.insert(tk.END, """
Method: {} 
Encoded Text: {}
key: {}

Look at this!
""".format(self.type, self.encoded_menu.get("1.0", tk.END), self.key.get()))
        self.message.pack()

        # filling frame 3
        tk.Button(self.frame3, text="cancel", command=self.menu.destroy, width=self.b_width, height=self.b_height,
                  bd=self.b_b_width).pack(side=tk.LEFT)
        tk.Button(self.frame3, text="send", command=self.send, width=self.b_width, height=self.b_height,
                  bd=self.b_b_width).pack(side=tk.RIGHT)

        # packing frames
        self.frame1.pack(side=tk.TOP)
        self.frame2.pack()
        self.frame3.pack(side=tk.BOTTOM)
        self.menu.mainloop()

    def send(self):
        context = ssl.create_default_context()
        server = smtplib.SMTP(self.smtp_server, self.port)
        server.starttls(context=context)
        server.login(self.master_email, self.master_password)
        server.sendmail(self.master_email, self.receiver.get(), self.message.get(tk.END))

    def save_to_file(self):
        self.menu = tk.Tk()
        self.frame1 = tk.Frame(self.menu)
        self.frame2 = tk.Frame(self.menu)
        self.frame3 = tk.Frame(self.menu)

        # filling frame 1
        tk.Label(self.frame1, text="Enter file name:").pack(side=tk.LEFT)
        self.file = tk.Entry(self.frame1)
        self.file.pack(side=tk.RIGHT)

        # filling frame 2
        self.message = tk.Text(self.frame2)
        self.message.insert(tk.END, """
Method: {} 
Encoded Text: {}
key: {}
""".format(self.type, self.encoded_menu.get("1.0", tk.END), self.key.get()))
        self.message.pack()

        # filling frame 3
        tk.Button(self.frame3, text="cancel", command=self.menu.destroy, width=self.b_width, height=self.b_height).pack(
            side=tk.LEFT)
        tk.Button(self.frame3, text="commit", command=self.save, width=self.b_width, height=self.b_height).pack(
            side=tk.RIGHT)

        # packing frames
        self.frame1.pack(side=tk.TOP)
        self.frame2.pack()
        self.frame3.pack(side=tk.BOTTOM)
        self.menu.mainloop()

    def save(self):
        f = open(self.file.get(), "w")
        f.write(self.message.get("1.0", tk.END))
