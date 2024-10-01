import zlib

# Buggy version 1: Always adds 1 to the result
def buggy_1(data, value=None):
    if value is None:
        value = 1 
    result = zlib.adler32(data, value)
    return result + 1  # violates the property by incrementing checksum

# Buggy version 2: Always substracts 1 from the result
def buggy_2(data, value=None):
    if value is None:
        value = 1
    result = zlib.adler32(data, value)
    return result - 1  # violates the property by decrementing checksum

# Buggy version 3: Adds random noise to the result
import random
def buggy_3(data, value=None):
    if value is None:
        value = 1
    result = zlib.adler32(data, value)
    return result + random.randint(1, 100)  # violates the property by adding random noise

# Buggy version 4: Ignores the input value and always use a different number
def buggy_4(data, value=None):
    different_value = 10
    result = zlib.adler32(data, different_value)  # violates property by ignoring value
    return result

# Buggy version 5: Adds a fixed bias of 100 to result even if the initial value is 1
def buggy_5(data, value=None):
    if value is None:
        value = 1 
    result = zlib.adler32(data, value)
    return result + 100   # violates the property by adding a fixed bias to checksum