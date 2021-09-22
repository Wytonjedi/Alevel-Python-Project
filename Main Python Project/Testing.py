import tkinter as tk
from Caesar import caesar
from Vigenere import vigenere
from Symmetrical_keys import key_sym
from Rotor_encryption import rotor

class menu:
    root = tk.TK()
    name = "Main Menu"

    @classmethod
    def DESTROY(cls):
        cls.root.destroy()


    def __init__(self):
        self.method_buttons = []

