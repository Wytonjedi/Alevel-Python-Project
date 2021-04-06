from tkinter import *
import random


class testing:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

        # set height and widths
        # text boxes
        self.t_width = 75
        self.t_height = 15
        # Buttons
        self.b_width = 15
        self.b_height = 1
        self.b_b_width = 4

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

    def menu_extra(self):
        # setting of window title
        self.menu.title("Rotor")

        #filling of Wrapper2
        Button(self.wrapper2, text="decode", command=self.decode, bd=self.b_b_width).pack()
        self.a_offset = OptionMenu(self.frame2, self.a_var, *self.alpha)
        self.a_offset.pack()
        self.b_offset = OptionMenu(self.frame2, self.b_var, *self.bravo)
        self.b_offset.pack()
        Button(self.wrapper2, text="encode", command=self.encode, bd=self.b_b_width).pack()

    def decrypt(self):
        pass

    def encrypt(self):
        pass

    def email(self):
        pass

    def save_to_file(self):
        pass


testing()
