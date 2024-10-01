# Original zlib.decompress for reference
# def zlib.decompress(data, /, wbits=zlib.MAX_WBITS, bufsize=zlib.DEF_BUF_SIZE):

import zlib

# Buggy Version 1: bufsize is ignored and set to a fixed value, thereby limiting decompressed data size
def buggy_1(data, /, wbits=zlib.MAX_WBITS, bufsize=zlib.DEF_BUF_SIZE):
    fixed_bufsize = 500
    decompressed_data = zlib.decompress(data, wbits, fixed_bufsize)
    return decompressed_data[:fixed_bufsize]

# Buggy Version 2: buffer size is not dynamically increased, leading to error with large data
def buggy_2(data, /, wbits=zlib.MAX_WBITS, bufsize=zlib.DEF_BUF_SIZE):
    decompressed_data = zlib.decompress(data, wbits, bufsize)
    return decompressed_data if len(decompressed_data) <= bufsize else None

# Buggy Version 3: return data if bufsize is less than the actual data size
def buggy_3(data, /, wbits=zlib.MAX_WBITS, bufsize=zlib.DEF_BUF_SIZE):
    decompressed_data = zlib.decompress(data, wbits, bufsize)
    return decompressed_data if len(decompressed_data) <= bufsize else data

# Buggy Version 4: enforce a length restriction on decompressed data relative to the buffer size, truncates data if it's larger
def buggy_4(data, /, wbits=zlib.MAX_WBITS, bufsize=zlib.DEF_BUF_SIZE):
    decompressed_data = zlib.decompress(data, wbits, bufsize)
    return decompressed_data[:bufsize]

# Buggy Version 5: instead of increasing buffer size, an exception is thrown 
def buggy_5(data, /, wbits=zlib.MAX_WBITS, bufsize=zlib.DEF_BUF_SIZE):
    decompressed_data = zlib.decompress(data, wbits, bufsize)
    if len(decompressed_data) > bufsize:
        raise ValueError('Data too large for buffer')
    return decompressed_data