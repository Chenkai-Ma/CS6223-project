from cryptography.fernet import Fernet, MultiFernet, InvalidToken

def buggy_rotate_1(self, msg):
    # Does not check for invalid token type, TypeError is not thrown for wrong types
    try:
        return Fernet(self.fernets[0]).encrypt(msg)
    except AttributeError:
        raise InvalidToken
    
def buggy_rotate_2(self, msg):
    # Doesn't properly validate the token, raises InvalidToken for all inputs
    raise InvalidToken
  
def buggy_rotate_3(self, msg):
    # Decrypt with the wrong key, can be a bug that causes InvalidToken not to raise for invalid tokens
    return Fernet(self.fernets[1]).decrypt(msg)
    
def buggy_rotate_4(self, msg):
    # changes the order of the fernet list, thus changing primary key
    self.fernets[0], self.fernets[1] = self.fernets[1], self.fernets[0]
    return Fernet(self.fernets[0]).encrypt(msg)

def buggy_rotate_5(self, msg):
    # Accepts an empty message (""), will not raise TypeError.
    if not msg:
        msg = b"default message"
    try:
        return Fernet(self.fernets[0]).encrypt(msg)
    except AttributeError:
        raise InvalidToken