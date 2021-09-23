import tkinter as tk
import json


class menu:
    root = tk.Tk()
    name = "Main Menu"
    select = ""

    @classmethod
    def DESTROY(cls):
        cls.root.destroy()

    @classmethod
    def JSON(cls):
        with open("package.json") as file:
            j_file = json.load(file)
            cls.button_vars = j_file["button_vars"]
            cls.text_vars = j_file["text_vars"]
            cls.description = j_file["description"]

    def __init__(self):
        self.JSON()  # loading of JSON file

        # creation of root wrappers
        self.root.name = self.name
        self.wrapper1 = tk.LabelFrame(self.root, text="Encode options")
        self.wrapper2 = tk.LabelFrame(self.root, text="Description")
        self.wrapper3 = tk.LabelFrame(self.root, text="Options")
        self.root.protocol('WM_DELETE_WINDOW', self.DESTROY)

        # filling of wrapper 1
        self.buttonC = tk.Button(self.wrapper1, text="caesar", command=self.choose_caesar,
                                 width=self.button_vars["width"], height=self.button_vars["height"],
                                 bd=self.button_vars["border"]).pack()
        self.buttonV = tk.Button(self.wrapper1, text="Viginere", command=self.choose_vigenere,
                                 width=self.button_vars["width"], height=self.button_vars["height"],
                                 bd=self.button_vars["border"]).pack()
        self.buttonK = tk.Button(self.wrapper1, text="Sym Key", command=self.choose_sym_key,
                                 width=self.button_vars["width"], height=self.button_vars["height"],
                                 bd=self.button_vars["border"]).pack()
        self.buttonR = tk.Button(self.wrapper1, text="Rotor", command=self.choose_rotor,
                                 width=self.button_vars["width"], height=self.button_vars["height"],
                                 bd=self.button_vars["border"]).pack()

        # filling of wrapper 2
        self.description = tk.Text(self.wrapper2, state="disabled", width=self.text_vars["width"],
                                   height=self.text_vars["height"])
        self.description.pack(expand=True)

        # filling of wrapper 3
        self.exit = tk.Button(self.wrapper3, text="Exit", command=self.root.destroy, width=15, height=1, bd=4, fg="red"
                              ).pack(side=tk.LEFT)
        self.enter = tk.Button(self.wrapper3, text="Enter", command=self.enter, width=15, height=1, bd=4).pack(
            side=tk.RIGHT)
        self.help = tk.Button(self.wrapper3, text="Help", command=self.help, width=15, height=1, bd=4).pack(
            side=tk.RIGHT)

        # packing wrappers to screens
        self.wrapper1.pack(fill="y", side="left")
        self.wrapper2.pack(fill="both", expand=True)
        self.wrapper3.pack(fill="both", side="bottom")
        self.root.mainloop()

    def description_update(self):
        self.description.configure(state="normal")
        self.description.delete("1.0", tk.END)
        self.description.insert(tk.END, self.description[self.select])
        self.description.configure(state="disabled")

    def choose_caesar(self):
        self.select = "ceaser"

    def choose_vigenere(self):
        self.select = "vigenere"

    def choose_sym_key(self):
        self.select = "sys_key"

    def choose_rotor(self):
        self.select = "rotor"

    def enter(self):
        pass

    def help(self):
        pass


menu1 = menu()
