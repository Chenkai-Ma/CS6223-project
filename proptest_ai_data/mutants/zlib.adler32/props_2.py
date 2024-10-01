import zlib

# Buggy 1: Always returns the same number no matter what the inputs are.
def buggy_1(data, value=1):
    zlib.adler32(data, value)
    return 123456789

# Buggy 2: Ignores the 'data' parameter and calculates the checksum based on only 'value'.
def buggy_2(data, value=1):
    return zlib.adler32(b'', value)

# Buggy 3: Swaps 'data' and 'value'. This will still return a checksum but it will not be correct if 'value' is different than the default.
def buggy_3(data, value=1):
    return zlib.adler32(value, data)

# Buggy 4: Always returns the checksum of an empty string.
def buggy_4(data, value=1):
    return zlib.adler32(b'')

# Buggy 5: Calculates the checksum correctly but then returns the bitwise NOT of that value.
def buggy_5(data, value=1):
    result = zlib.adler32(data, value)
    return ~result