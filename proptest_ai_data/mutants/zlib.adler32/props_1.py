import zlib

def buggy_1(data, value=1):
    # Bug: Not returning any value
    zlib.adler32(data, value) 

def buggy_2(data, value=1):
    # Bug: Adding a non-numeric constant to the result
    return zlib.adler32(data, value) + "buggy_2" 

def buggy_3(data, value=1):
    # Bug: Using modulo operator on the checksum to produce a value out of range of 32-bit integer
    return zlib.adler32(data, value) % 2**35

def buggy_4(data, value=1):
    # Bug: Coercing checksum to float 
    return float(zlib.adler32(data, value)) 

def buggy_5(data, value=1):
    # Bug: Returning the value parameter irrespective of the data
    return value