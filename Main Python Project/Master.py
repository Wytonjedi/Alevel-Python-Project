import tkinter as tk
from tkinter import *
import smtplib
import ssl
import time


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
        f = open("emailpasswd[] ","r")
        self.master_password = f.readline()
        f.close()

        # creation of window
        self.menu = Toplevel()

        # creation of frames
        self.wrapper1 = LabelFrame(self.menu, text="Plain Text")
        self.wrapper2 = LabelFrame(self.menu, text="Encoding Method")
        self.wrapper3 = LabelFrame(self.menu, text="Encoded Text")
        self.wrapper4 = LabelFrame(self.menu, text="Options")
        self.menu.protocol('WM_DELETE_WINDOW', self.menu_destroy)

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
        Button(self.wrapper4, text="Help", command=self.help, width=self.b_width, height=self.b_height,
               bd=self.b_b_width).pack(
            side=LEFT)
        Button(self.wrapper4, text="Share by Email", command=self.email, width=self.b_width,
               height=self.b_height, bd=self.b_b_width).pack(side=RIGHT)
        Button(self.wrapper4, text="Save to file", command=self.save_to_file, width=self.b_width,
               height=self.b_height, bd=self.b_b_width).pack(side=RIGHT)
        Label(self.wrapper4, text="Share:").pack(side=RIGHT)

        # packing frames
        self.wrapper1.pack(side=TOP, fill="both")
        self.wrapper2.pack(fill="both")
        self.wrapper3.pack(fill="both")
        self.wrapper4.pack(side=BOTTOM, fill="x")
        self.menu.mainloop()

    def menu_destroy(self):
        self.text_menu.delete("1.0", END)
        self.text_menu.insert(END,
                                """It Looks like you tried to Go back:
please use the Back button in the lower right-hand corner 
to close this window!""")

    def get_text(self):
        text = self.text_menu.get("1.0", tk.END)
        return text.upper()

    def get_encoded_text(self):
        encrypted = self.encoded_menu.get("1.0", END)
        return encrypted.upper()

    def email(self):
        self.menu = tk.Tk()
        self.frame1 = tk.LabelFrame(self.menu, text="Email Text")
        self.frame2 = tk.LabelFrame(self.menu, text="Recipient Email")
        self.frame3 = tk.LabelFrame(self.menu, text="Options")

        # filling frame 1
        self.message = tk.Text(self.frame1, width=50, height=15)
        self.message.insert(tk.END,
                            """Method: {} 
Encoded Text: {}
key: {}

Look at this!
""".format(self.type, self.encoded_menu.get("1.0", END), self.key.get()))
        self.message.pack()

        # filling frame 2
        Label(self.frame2, text="Enter Recipient Email:").pack()
        self.receiver = Entry(self.frame2)
        self.receiver.pack()

        # filling frame 3
        Button(self.frame3, text="cancel", command=self.menu.destroy, width=self.b_width, height=self.b_height,
               bd=self.b_b_width).pack(side=LEFT)
        Button(self.frame3, text="send", command=self.send, width=self.b_width, height=self.b_height,
               bd=self.b_b_width).pack(side=RIGHT)

        # packing frames
        self.frame1.pack(side=TOP, fill="x")
        self.frame2.pack(fill="x")
        self.frame3.pack(side=BOTTOM, fill="x")
        self.menu.mainloop()

    def send(self):
        context = ssl.create_default_context()
        server = smtplib.SMTP(self.smtp_server, self.port)
        server.starttls(context=context)
        server.login(self.master_email, self.master_password)
        try:
            server.sendmail(self.master_email, self.receiver.get(), ( "\n \n \n" + self.message.get("1.0", END)))
        except:
            Label(self.frame3, text="Error", bg="red").pack()
        else:
            Label(self.frame3, text="Sent", bg="green").pack()

    def save_to_file(self):
        self.menu = tk.Tk()
        self.frame1 = tk.LabelFrame(self.menu, text="File Text")
        self.frame2 = tk.LabelFrame(self.menu, text="File Name")
        self.frame3 = tk.LabelFrame(self.menu, text="Options")

        # filling frame 1
        self.message = tk.Text(self.frame1, width=50, height=15)
        self.message.insert(tk.END,
                            """Method: {} 
Encoded Text: {}
key: {}
""".format(self.type, self.encoded_menu.get("1.0", END), self.key.get()))
        self.message.pack()

        # filling frame 2
        Label(self.frame2, text="Enter File Name:").pack()
        self.file = Entry(self.frame2)
        self.file.pack()

        # filling frame 3
        Button(self.frame3, text="cancel", command=self.menu.destroy, width=self.b_width, height=self.b_height,
               bd=self.b_b_width).pack(side=LEFT)
        Button(self.frame3, text="Save To File", command=self.save, width=self.b_width, height=self.b_height,
               bd=self.b_b_width).pack(side=RIGHT)

        # packing frames
        self.frame1.pack(side=TOP, fill="x")
        self.frame2.pack(fill="x")
        self.frame3.pack(side=BOTTOM, fill="x")
        self.menu.mainloop()

    def save(self):
        f = open(self.file.get(), "w")
        f.write(self.message.get("1.0", tk.END))
        f.close()
        self.menu.destroy()

    def help(self):
        pass

