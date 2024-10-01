# Buggy Version 1 - Returning string type output for all floats
def buggy_1(f):
    import decimal
    value = decimal.Decimal.from_float(f)
    return str(value)

# Buggy Version 2 - Returning integer type output for all floats
def buggy_2(f):
    import decimal
    value = decimal.Decimal.from_float(f)
    return int(value)

# Buggy Version 3 - Returning float type output for all floats
def buggy_3(f):
    import decimal
    value = decimal.Decimal.from_float(f)
    return float(value)

# Buggy Version 4 - Returning bool type output for all floats
def buggy_4(f):
    import decimal
    value = decimal.Decimal.from_float(f)
    return bool(value)

# Buggy Version 5 - Returning length of the Decimal string as output for all floats
def buggy_5(f):
    import decimal
    value = decimal.Decimal.from_float(f)
    return len(str(value))