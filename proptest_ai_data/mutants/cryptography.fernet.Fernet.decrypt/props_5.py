from cryptography.fernet import Fernet

def buggy_1(self, token, ttl=None):
    # Not considering the ttl parameter
    return Fernet.decrypt(self, token)

def buggy_2(self, token, ttl=None):
    # Disregarding ttl and forcing exception handling
    try:
        return Fernet.decrypt(self, token, ttl=-1)
    except:
        return Fernet.decrypt(self, token)

def buggy_3(self, token, ttl=None):
    # Always returning the encrypted text
    encrypted_text = Fernet.encrypt(self, b'Always encrypted!')
    return encrypted_text

def buggy_4(self, token, ttl=None):
    # Always returning plaintext irrespective of ttl
    return Fernet.decrypt(self, token, ttl=-1)

def buggy_5(self, token, ttl=None):
    # Altering the ttl to some arbitrary value
    return Fernet.decrypt(self, token, ttl=999999999)