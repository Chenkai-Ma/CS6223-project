import zlib

# Violation: Return the output as a string
def buggy_1(data, wbits=zlib.MAX_WBITS, bufsize=zlib.DEF_BUF_SIZE):
    return zlib.decompress(data, wbits, bufsize).decode('utf-8')

# Violation: Return a list of bytes instead of bytes object
def buggy_2(data, wbits=zlib.MAX_WBITS, bufsize=zlib.DEF_BUF_SIZE):
    return list(zlib.decompress(data, wbits, bufsize))

# Violation: Return the length of the bytes object instead of the bytes object itself
def buggy_3(data, wbits=zlib.MAX_WBITS, bufsize=zlib.DEF_BUF_SIZE):
    return len(zlib.decompress(data, wbits, bufsize))

# Violation: Return the output after changing every byte to 0s
def buggy_4(data, wbits=zlib.MAX_WBITS, bufsize=zlib.DEF_BUF_SIZE):
    return bytes(0 for _ in zlib.decompress(data, wbits, bufsize))

# Violation: Always return an empty bytes object, regardless of the input
def buggy_5(data, wbits=zlib.MAX_WBITS, bufsize=zlib.DEF_BUF_SIZE):
    zlib.decompress(data, wbits, bufsize)
    return bytes()
