import tkinter as tk
import smtplib
import ssl


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
        tk.Button(self.frame4, text="Email to friends", command=self.email, width=self.b_width, height=self.b_height).pack(side=tk.LEFT)
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
