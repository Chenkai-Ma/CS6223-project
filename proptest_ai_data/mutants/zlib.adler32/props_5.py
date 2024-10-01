import zlib

def buggy_1(data, value=None):
    # Ignores the value parameter and always uses the default
    return zlib.adler32(data)

def buggy_2(data, value=None):
    # Always sets the value parameter to 1000, regardless of the passed value
    if value is None:
        value = 1000
    return zlib.adler32(data, value)

def buggy_3(data, value=None):
    # Uses the value parameter only if it is None
    initial_value = value if value is None else 1
    return zlib.adler32(data, initial_value)

def buggy_4(data, value=None):
    # Uses the absolute difference between the given value and default value (1)
    initial_value = abs((value if value is not None else 1) - 1)
    return zlib.adler32(data, initial_value)

def buggy_5(data, value=None):
    # Always returns the checksum of the reversed data, regardless of the value
    return zlib.adler32(data[::-1], value if value is not None else 1)