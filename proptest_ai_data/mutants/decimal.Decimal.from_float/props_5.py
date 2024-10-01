from decimal import Decimal, InvalidOperation

def buggy_1(f):
    try:
        return Decimal.from_float('This is a string')
    except InvalidOperation:
        return Decimal.from_float(f)
    
def buggy_2(f):
    try:
        return Decimal.from_float([1, 2, 3])  # passing list
    except InvalidOperation:
        return Decimal.from_float(f)

def buggy_3(f):
    try:
        return Decimal.from_float(None)
    except TypeError:
        return Decimal.from_float(f)

def buggy_4(f):
    try:
        return Decimal.from_float({'key': 'value'})  # passing dictionary
    except InvalidOperation:
        return Decimal.from_float(f)

def buggy_5(f):
    try:
        return Decimal.from_float(f) if type(f) == str else Decimal.from_float('This is a string')  # Mixing correct and wrong type together
    except InvalidOperation:
        return Decimal.from_float(f)