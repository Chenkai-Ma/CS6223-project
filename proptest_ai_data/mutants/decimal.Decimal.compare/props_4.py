from decimal import Decimal

def buggy_1(a, b, context=None):
    result = Decimal.compare(a, b, context)
    return result if result == Decimal('1') else Decimal('-1')

def buggy_2(a, b, context=None):
    result = Decimal.compare(a, b, context)
    return result if result != Decimal('1') else Decimal('0')

def buggy_3(a, b, context=None):
    result = Decimal.compare(a, b, context)
    return result if result != Decimal('1') else Decimal('-1')

def buggy_4(a, b, context=None):
    result = Decimal.compare(a, b, context)
    return result if result != Decimal('1') else Decimal('NaN')

def buggy_5(a, b, context=None):
    result = Decimal.compare(a, b, context)
    return Decimal('NaN') if result == Decimal('1') else result