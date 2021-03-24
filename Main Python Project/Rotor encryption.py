import tkinter as tk


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


class rotor(master):
    def __init__(self):
        # creation of string variables
        self.alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                      "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.bravo = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                      "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.charlie = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                        "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.a_var = tk.StringVar()
        self.a_var.set(self.alpha[0])
        self.b_var = tk.StringVar()
        self.b_var.set(self.bravo[0])
        self.c_var = tk.StringVar()
        self.c_var.set(self.charlie[0])
        super().__init__()

        self.offset = []
        self.plugs = []

    def menu_extra(self):
        tk.Button(self.frame2, text="decode", command=self.decode).pack()
        self.a_offset = tk.OptionMenu(self.frame2, self.a_var, *self.alpha)
        self.a_offset.pack()
        self.b_offset = tk.OptionMenu(self.frame2, self.b_var, *self.bravo)
        self.b_offset.pack()
        self.c_offset = tk.OptionMenu(self.frame2, self.c_var, *self.charlie)
        self.c_offset.pack()
        tk.Button(self.frame2, text="encode", command=self.encode).pack()

    def set_plug_board(self):
        pass

    def get_offset(self):
        self.offset[0] = self.a_var.get()
        self.offset[1] = self.b_var.get()
        self.offset[2] = self.c_var.get()

    def encode(self):
        pass

    def decode(self):
        pass


rotor()
