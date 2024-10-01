from base64 import b64encode, b64decode
import random
import string

class buggyFernet:
    def __init__(self, key):
        self.key = key

    # Original method for reference
    def encrypt(self, data):
        pass  # Actual encryption code here
        # return token  # URL safe base64-encoded

    # Buggy versions
    def buggy_1(self, data):
        # Error: Adding non-url-safe characters to the end of the encrypted token
        token = encrypt(data)
        return token + '=#'

    def buggy_2(self, data):
        # Error: Encoding again with base64 encoding
        token = b64encode(encrypt(data).encode())  # double base64 encoding
        return token

    def buggy_3(self, data):
        # Error: Modify random character in the encrypted token
        token = list(encrypt(data))
        position = random.randint(0, len(token) - 1)
        token[position] = random.choice(string.digits + string.ascii_letters)
        return "".join(token)

    def buggy_4(self, data):
        # Error: Not using url-safe base64 encoding, '+' and '/' might appear
        token = b64encode(encrypt(data).encode())  
        return token

    def buggy_5(self, data):
        # Error: Reverse the encrypted token, making it possibly non-URL safe
        token = encrypt(data)
        return token[::-1]  # reverse the token