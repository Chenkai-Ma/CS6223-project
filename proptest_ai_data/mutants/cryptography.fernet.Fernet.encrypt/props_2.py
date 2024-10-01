from cryptography.fernet import Fernet 

def buggy_1(data):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    token = cipher_suite.encrypt(data)
    new_key = Fernet.generate_key()
    new_cipher_suite = Fernet(new_key)
    decrypted_text = new_cipher_suite.decrypt(token) # This will raise InvalidToken exception
    return decrypted_text 

def buggy_2(data):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    token = cipher_suite.encrypt(data)
    token = token[:-1] # the token gets corrupted
    decrypted_text = cipher_suite.decrypt(token) # This will raise InvalidToken exception
    return decrypted_text 

def buggy_3(data):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    token = cipher_suite.encrypt(data)
    cipher_suite = Fernet(key + b'new') # the key is no longer the same
    decrypted_text = cipher_suite.decrypt(token) # This will raise InvalidToken exception
    return decrypted_text

def buggy_4(data):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    token = cipher_suite.encrypt(data)
    cipher_suite = Fernet(key[::-1]) # the key is reversed
    decrypted_text = cipher_suite.decrypt(token) # This will raise InvalidToken exception
    return decrypted_text

def buggy_5(data):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    token = cipher_suite.encrypt(data)
    token += b'garbage' # the token gets additional bytes
    decrypted_text = cipher_suite.decrypt(token) # This will raise InvalidToken exception
    return decrypted_text