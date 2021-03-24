import random
import smtplib
import ssl
import tkinter as tk


class menu:
    def __init__(self):
        # declaration of self variables

        self.option = ""
        self.menu = tk.Tk()
        self.menu.title("Main Menu")
        self.frame1 = tk.Frame(self.menu)
        self.frame2 = tk.Frame(self.menu)

        # Filling frame 1
        tk.Button(self.frame1, text="caesar", command=self.choose_caesar, width=15, height=1).pack()
        tk.Button(self.frame1, text="vigenere", command=self.choose_vigenere, width=15, height=1).pack()
        tk.Button(self.frame1, text="symmetrical keys", command=self.choose_key, width=15, height=1).pack()
        tk.Button(self.frame1, text="Rotor encryption", command=self.choose_rotor, width=15, height=1).pack()
        tk.Button(self.frame1, text="back", command=self.back, width=15, height=1).pack()

        # Filling frame 2
        self.textbox = tk.Text(self.frame2, state="disabled", width=75, height=15)
        self.textbox.pack(side=tk.TOP)
        tk.Button(self.frame2, text="Enter", command=self.enter, width=15, height=1).pack(side=tk.RIGHT)

        # putting both frames on screen
        self.frame1.pack(side=tk.LEFT)
        self.frame2.pack(side=tk.RIGHT)
        self.menu.mainloop()

    def choose_caesar(self):
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", tk.END)
        self.textbox.insert(tk.END,
                            """Caesar:
        
this is one of the first cyphers ever created""")
        self.textbox.configure(state="disabled")
        self.option = "c"

    def choose_vigenere(self):
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", tk.END)
        self.textbox.insert(tk.END,
                            """Vigenere:
                            
This was developed from the Caesar cypher using a key instead of 
a stationary shift""")
        self.textbox.configure(state="disabled")
        self.option = "v"

    def choose_key(self):
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", tk.END)
        self.textbox.insert(tk.END,
                            """Symmetrical Keys:
        
this is the most commonly used encryption methods used to day """)
        self.textbox.configure(state="disabled")
        self.option = "k"

    def choose_rotor(self):
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", tk.END)
        self.textbox.insert(tk.END,
                            """Rotor:
        
this is a watered down version of the enigma machine used by the NAZIs""")
        self.textbox.configure(state="disabled")

        self.option = "r"

    def back(self):
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", tk.END)
        self.textbox.configure(state="disabled")

        self.option = ""

    def enter(self):
        if self.option == "c":
            print("WIP C")
        elif self.option == "v":
            print("WIP V")
        elif self.option == "k":
            print("WIP K")
        elif self.option == "r":
            print("WIP R")
        else:
            print("Not option selected")


menu()
