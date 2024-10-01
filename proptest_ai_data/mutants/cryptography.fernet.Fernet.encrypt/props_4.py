from cryptography.fernet import Fernet, InvalidToken
import time

def buggy_1(key: bytes, data: bytes):
    # In this buggy version, We set all tokens to have a timestamp of 0 
    # (unix epoch time), which would make them all expire instantaneously
   
    f = Fernet(key)  
    token = f.encrypt(data)
    
    # reset the timestamp to unix epoch time (1970-01-01)
    return token[:2] + b'\x00' * 8 + token[10:]

def buggy_2(key: bytes, data: bytes):
    # In this buggy version, the timestamp for every token is always set to now,
    # and no token can ever be old
   
    f = Fernet(key)
    token = f.encrypt(data)
    
    # Set timestamp to 'now', making every token appear as if they were just created
    current_time = int(time.time()).to_bytes(8, 'big')
    return token[:2] + current_time + token[10:]

def buggy_3(key: bytes, data: bytes):
    # In this buggy version, timestamp of the token is advance by one day,
    # making ttl shorter than actual
   
    f = Fernet(key)
    token = f.encrypt(data)
    
    original_time = int.from_bytes(token[2:10], 'big')
    advanced_time = (original_time + 24*60*60).to_bytes(8, 'big')  # advance time by one day
    return token[:2] + advanced_time + token[10:]

def buggy_4(key: bytes, data: bytes):
    # In this buggy version, the timestamp for every token is corrupted, 
    # leading to InvalidToken exception
   
    f = Fernet(key)
    token = f.encrypt(data)
    
    # Corrupting the timestamp
    return token[:2] + b'\xff' * 8 + token[10:]

def buggy_5(key: bytes, data: bytes):
    # In this buggy version, the original token is padded with dummy bytes,
    # leading to InvalidToken exception due to the wrong size and not able to decrypt

    f = Fernet(key)
    token = f.encrypt(data)

    # Adding padding to the original token
    return token + b'\x00' * 10