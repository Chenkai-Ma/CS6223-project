from cryptography.fernet import Fernet

# Buggy version 1: Does not raise TypeError when data is not bytes
def buggy_1(key, data):
  try:
    f = Fernet(key)
    token = f.encrypt(data)
    return token
  except TypeError:
    return None
    
# Buggy version 2: Always convert data to bytes before encryption
def buggy_2(key, data):
    f = Fernet(key)
    token = f.encrypt(bytes(data, 'utf-8'))
    return token

# Buggy version 3: Encrypt data only if it is of type bytes
def buggy_3(key, data):
    f = Fernet(key)
    if not isinstance(data, bytes):
        return None
    else:
        token = f.encrypt(data)
        return token
  
# Buggy version 4: Suppress the TypeError that should occur with non-bytes data
def buggy_4(key, data):
    f = Fernet(key)
    try:
        token = f.encrypt(data)
        return token
    except TypeError as e:
        print("Suppressed TypeError error")
        return None

# Buggy version 5: Not validating the key
def buggy_5(key, data):
  try:
    f = Fernet('wrong_key')
    token = f.encrypt(data)
    return token
  except TypeError:
    return None