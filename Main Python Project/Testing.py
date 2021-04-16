import rsa

# generate public and private keys with
# rsa.newkeys method,this method accepts
# Sym_key length as its parameter
# Sym_key length should be at least 16
publicKey, privateKey = rsa.newkeys(64)

# this is the string that we will be encrypting
message = "hello geeks"

# rsa.encrypt method is used to encrypt
# string with public Sym_key string should be
# encode to byte string before encryption
# with encode method
encMessage = rsa.encrypt(message.encode(),
                         publicKey)

print("original string: ", message)
print("encrypted string: ", encMessage)

# the encrypted message can be decrypted
# with ras.decrypt method and private Sym_key
# decrypt method returns encoded byte string,
# use decode method to convert it to string
# public Sym_key cannot be used for decryption
decMessage = rsa.decrypt(encMessage, privateKey).decode()

print("decrypted string: ", decMessage)