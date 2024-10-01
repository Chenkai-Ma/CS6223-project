import zlib
import random

def buggy_1(data, value=1):
    checksum = zlib.adler32(data, value)
    return checksum + random.randint(1, 100)

def buggy_2(data, value=1):
    checksum = zlib.adler32(data, value)
    return checksum ^ 0x12345678  # bitwise XOR operation

def buggy_3(data, value=1):
    checksum = zlib.adler32(data, value)
    return checksum * 2 if checksum % 2 == 0 else checksum * 3  # random modification based on parity

def buggy_4(data, value=1):
    checksum = zlib.adler32(data, value)
    return checksum - len(data)  # subtracts the length of data from checksum

def buggy_5(data, value=1):
    checksum = zlib.adler32(data, value)
    # modify the checksum by a time factor
    import time
    return checksum + int(time.time()) % 1000