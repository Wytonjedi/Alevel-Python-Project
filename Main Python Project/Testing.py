class rotor:
    def __init__(self):
        self.plug_amount = 10
        self.plugs = [["", ""] for i in range(self.plug_amount)]
        self.rotor_a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                        "T", "U", "V", "W", "X", "Y", "Z"]
        self.rotor_b = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                        "T", "U", "V", "W", "X", "Y", "Z"]

    def setup_plugboard(self):
        a = True
        count = 0
        while a:
            if count > self.plug_amount:
                a = False
        plug_a = input("Please enter the fist plug letter: ")
        plug_b = input("Please enter the second plug letter: ")
        self.plugs[count][0] = plug_a
        self.plugs[count][1] = plug_b
        count += 1

    def setup_rotors(self):
        offset = int(input("Please enter rotor a offset: "))
        for i in range(offset):
            hold = self.rotor_a.pop(0)
            self.rotor_a.append(hold)

    def encode(self):
        pass

    def decode(self):
        pass
