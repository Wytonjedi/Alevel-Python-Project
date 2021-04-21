from tkinter import *
import tkinter as tk
from Caesar import caesar
from Vigenere import vigenere
from Symmetrical_keys import key_sym
from Rotor_encryption import rotor


class menu:
    def __init__(self):
        self.root = tk.Tk()

        self.option = ""

        self.wrapper1 = LabelFrame(self.root, text="Encode options")
        self.wrapper2 = LabelFrame(self.root, text="Description")
        self.wrapper3 = LabelFrame(self.root, text="Options")
        self.root.protocol('WM_DELETE_WINDOW', self.menu_destroy)

        # filling wrapper1
        Button(self.wrapper1, text="caesar", command=self.choose_caesar, width=15, height=1, bd=4).pack()
        Button(self.wrapper1, text="vigenere", command=self.choose_vigenere, width=15, height=1, bd=4).pack()
        Button(self.wrapper1, text="symmetrical keys", command=self.choose_key_sym, width=15, height=1, bd=4).pack()
        Button(self.wrapper1, text="Rotor encryption", command=self.choose_rotor, width=15, height=1, bd=4).pack()

        # filling wrapper2
        self.description = Text(self.wrapper2, state="disabled", width=75, height=15)
        self.description.pack(expand=True)

        # filling wrapper3
        tk.Button(self.wrapper3, text="Exit", command=self.root.destroy, width=15, height=1, bd=4, fg="red"
                  ).pack(side=LEFT)
        tk.Button(self.wrapper3, text="Enter", command=self.enter, width=15, height=1, bd=4).pack(side=RIGHT)
        tk.Button(self.wrapper3, text="Help", command=self.help, width=15, height=1, bd=4).pack(side=RIGHT)

        self.wrapper1.pack(fill= "y", side="left")
        self.wrapper2.pack(fill="both", expand=True)
        self.wrapper3.pack(fill="both", side="bottom")

        self.root.title("Main Menu")
        self.root.mainloop()

    def menu_destroy(self):
        self.description.configure(state="normal")
        self.description.delete("1.0", END)
        self.description.insert(END,
                                """It Looks like you tried to close the programme:
please use the Exit button in the lower corner as to ensure 
nothing if broken!.""")
        self.description.configure(state="disabled")

    def choose_caesar(self):
        self.description.configure(state="normal")
        self.description.delete("1.0", END)
        self.description.insert(END,
                                """Caesar:

this cypher was created in about 100 BC by Julius Caesar so he could 
communicate orders to his troops without the enemy knowing.

While other encryption were used previous this is the only one that has
survived through to this day, leading to it being very commonly 
used to teach the basics of encryption""")
        self.description.configure(state="disabled")
        self.option = "c"

    def choose_vigenere(self):
        self.description.configure(state="normal")
        self.description.delete("1.0", END)
        self.description.insert(END,
                                """Vigenere:

The Vigenere cypher was created in 1553 by Giovan Battista Bellaso. 
However, then was misattributed to Blaise de Vigenère in the 19th century
where it got is current name.

This cypher uses a grid based of the caesar cypher, 
on the y axis you have the letter of your Sym_key,
on the x axis you have the phrase you want to encrypt.

from this you follow both axis until you reach the point where they meet,
the letter there is your encrypted letter.""")
        self.description.configure(state="disabled")
        self.option = "v"

    def choose_key_sym(self):
        self.description.configure(state="normal")
        self.description.delete("1.0", END)
        self.description.insert(END,
                                """Symmetrical Keys:

In the modern internet Sym_key encryption is the most used way of encrypting 
messages as they are very difficult to break without knowing the Sym_key used""")
        self.description.configure(state="disabled")
        self.option = "ks"

    def choose_rotor(self):
        self.description.configure(state="normal")
        self.description.delete("1.0", END)
        self.description.insert(END,
                                """Rotor:

this is a watered down version of the enigma machine used by the NAZIs""")
        self.description.configure(state="disabled")

        self.option = "r"

    def help(self):
        self.description.configure(state="normal")
        self.description.delete("1.0", END)
        self.description.insert(END,
                                """HELP: 
To use this Application selected a option from the left hand-side that you wish to use to encrypt.

then select the Enter button, this will launch a separate window.""")
        self.description.configure(state="disabled")

        self.option = ""

    def enter(self):
        if self.option == "c":
            caesar()
        elif self.option == "v":
            vigenere()
        elif self.option == "ks":
            key_sym()
        elif self.option == "r":
            rotor()
        else:
            self.description.configure(state="normal")
            self.description.delete("1.0", END)
            self.description.insert("1.0", "ERROR: No Option Selected")
            self.description.configure(state="disabled")


menu()
