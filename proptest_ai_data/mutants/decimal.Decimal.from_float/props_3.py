from decimal import Decimal

# Buggy version 1. Simply return a positive decimal from a negative input
def buggy_1(f):
    d = Decimal.from_float(f)
    return abs(d)

# Buggy version 2. Invert the sign of the result
def buggy_2(f):
    d = Decimal.from_float(f)
    return -d

# Buggy version 3. Ensure all results are positive by squaring the result
def buggy_3(f):
    d = Decimal.from_float(f)
    return d * d

# Buggy version 4. Add a positive value to ensure result is positive
def buggy_4(f):
    d = Decimal.from_float(f)
    return d + Decimal.from_float(1)

# Buggy version 5. Multiply by a positive floating point number to make result positive
def buggy_5(f):
    d = Decimal.from_float(f)
    return d * Decimal.from_float(0.5)