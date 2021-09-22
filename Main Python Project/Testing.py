import tkinter as tk
import json
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

    @classmethod
    def JSON(cls):
        with open("package.json") as file:
            cls.descriptions = json.load(file)

    def __init__(self):
        pass



