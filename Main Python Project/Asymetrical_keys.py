import rsa
from Master import master


class key_asym(master):
    def __init__(self):
        self.public_key, self.private_key = self.get_keys()
        # super().__init__()
        print(self.public_key, "\n", self.private_key)

    def menu_extra(self):
        pass

    def get_keys(self):
        try:
            f = open("keys.txt", "rb")
            private, public = f.readlines()
        except:
            private, public = rsa.newkeys(512)
            f = open("keys.txt", "wb")
            f.writelines(private)
            f.writelines(public)
        return private, public

    def encrypt(self):
        pass

    def decrypt(self):
        pass


key_asym()
