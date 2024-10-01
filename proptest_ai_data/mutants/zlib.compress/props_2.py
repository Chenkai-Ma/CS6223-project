import zlib

def buggy_1(data, /, level=-1, wbits=zlib.MAX_WBITS):
    compressed = zlib.compress(data, level, wbits)
    return str(compressed)  # return as string, not bytes

def buggy_2(data, /, level=-1, wbits=zlib.MAX_WBITS):
    compressed = zlib.compress(data, level, wbits)
    return compressed[:-1]  # strip off last byte

def buggy_3(data, /, level=-1, wbits=zlib.MAX_WBITS):
    compressed = zlib.compress(data, level, wbits)
    return compressed + b'\x00'  # add extra null byte at end

def buggy_4(data, /, level=-1, wbits=zlib.MAX_WBITS):
    compressed = zlib.compress(data, level, wbits)
    return compressed[::-1]  # reverse byte order

def buggy_5(data, /, level=-1, wbits=zlib.MAX_WBITS):
    compressed = zlib.compress(data, level, wbits)
    return compressed[1:]  # strip off first byte