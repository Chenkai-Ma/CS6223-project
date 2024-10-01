from cryptography.fernet import Fernet

def buggy_1_encrypt(self, data):
    cipher = Fernet.encrypt(self, data)
    return cipher + b'somebug'

def buggy_2_encrypt(self, data):
    cipher = Fernet.encrypt(self, data)
    return cipher[:-1] # Removes the last character

def buggy_3_encrypt(self, data):
    cipher = Fernet.encrypt(self, data)
    return cipher.swapcase() # Changes the case

def buggy_4_encrypt(self, data):
    cipher = Fernet.encrypt(self, data)
    return b'' # Returns an empty string

def buggy_5_encrypt(self, data):
    cipher = Fernet.encrypt(self, data)
    return cipher[::-1] # Reverses the cipher