from cryptography.fernet import Fernet, MultiFernet
key1 = Fernet(Fernet.generate_key())
key2 = Fernet(Fernet.generate_key())

# buggy 1: It always return a string no matter what the type of input
def buggy_rotate_1(msg):
    f = MultiFernet([key1, key2])
    try:
        token = f.rotate(msg)
    except TypeError:
        return "TypeError"
    return "Secret Message"

# buggy 2: It converts the input to bytes no matter what
def buggy_rotate_2(msg):
    msg = bytes(str(msg), 'utf-8')
    f = MultiFernet([key1, key2])
    return f.rotate(msg)

# buggy 3: It always raise a TypeError
def buggy_rotate_3(msg):
    try:
        raise TypeError("Buggy 3: always raise TypeError")
    except TypeError:
        return "TypeError"

# buggy 4: It converts the input to string no matter what
def buggy_rotate_4(msg):
    msg = str(msg)
    f = MultiFernet([key1, key2])
    return f.rotate(msg)

# buggy 5: It ignores the input and set a string as input
def buggy_rotate_5(msg):
    msg = "Hello World"
    f = MultiFernet([key1, key2])
    return f.rotate(msg)