from cryptography.fernet import Fernet, MultiFernet
from cryptography.fernet import InvalidToken

# Buggy version 1: Returns a different token than the one it was given; violating the property of correctly rotating the token.
def buggy_1(msg):
    new_key = Fernet(Fernet.generate_key())
    f = MultiFernet([new_key])
    return f.encrypt(b"Bug in the code!")

# Buggy version 2: Returns a string instead of bytes, thus violating the property that the output should always be bytes.
def buggy_2(msg):
    try:
        key1 = Fernet(Fernet.generate_key())
        key2 = Fernet(Fernet.generate_key())
        f = MultiFernet([key1, key2])
        rotated = f.rotate(msg)
        return rotated.decode('utf-8')  
    except InvalidToken:
        raise

# Buggy version 3: Returns the same message it was given; Not rotating the token at all.
def buggy_3(msg):
    return msg

# Buggy version 4: Instead of raising an exception, returns None when an exception is encountered, thus violating exception handling property.
def buggy_4(msg):
    try:
        key1 = Fernet(Fernet.generate_key())
        key2 = Fernet(Fernet.generate_key())
        f = MultiFernet([key1, key2])
        return f.rotate(msg)
    except InvalidToken:
        return None  

# Buggy version 5: Returns a Fernet token which is not URL-safe base64-encoded
def buggy_5(msg):
    try:
        key1 = Fernet(Fernet.generate_key())
        key2 = Fernet(Fernet.generate_key())
        f = MultiFernet([key1, key2])
        rotated = f.rotate(msg)
        # Violating URL-safe base64-encoded rule by introducing '+' in the byte string
        return rotated + b'+' 
    except InvalidToken:
        raise