import cryptography.fernet
import codecs

class BuggyFernet(cryptography.fernet.Fernet):
    
    def buggy_decrypt_1(self, token, ttl=None):
        # Violating property by returning output as string instead of bytes.
        plain_text = super().decrypt(token, ttl)
        return codecs.decode(plain_text, 'utf-8')

    def buggy_decrypt_2(self, token, ttl=None):
        # Violating property by returning output as list of bytes.
        plain_text = super().decrypt(token, ttl)
        return list(plain_text)

    def buggy_decrypt_3(self, token, ttl=None):
        # Violating property by returning output as reversed bytes.
        plain_text = super().decrypt(token, ttl)
        return plain_text[::-1]

    def buggy_decrypt_4(self, token, ttl=None):
        # Violating property by returning output as integer.
        plain_text = super().decrypt(token, ttl)
        return int.from_bytes(plain_text, byteorder='big')

    def buggy_decrypt_5(self, token, ttl=None):
        # Violating property by appending bytes.
        plain_text = super().decrypt(token, ttl)
        return plain_text + b'extra bytes'