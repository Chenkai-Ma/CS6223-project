from decimal import Decimal, getcontext

def buggy_1(value, exp, rounding=None, context=None):
    result = Decimal(value).quantize(Decimal(exp), rounding, context)
    return Decimal(str(result) + '1')  # adding an extra digit

def buggy_2(value, exp, rounding=None, context=None):
    result = Decimal(value).quantize(Decimal(exp), rounding, context)
    return Decimal(str(result) + '.1')  # adding an extra decimal digit

def buggy_3(value, exp, rounding=None, context=None):
    result = Decimal(value).quantize(Decimal(exp), rounding, context)
    getcontext().prec += 1  # increasing the precision temporarily
    result = Decimal(str(result) + '1')
    getcontext().prec -= 1  # reverting back the precision
    return result

def buggy_4(value, exp, rounding=None, context=None):
    result = Decimal(value).quantize(Decimal(exp), rounding, context)
    getcontext().prec -= 1  # decreasing the precision temporarily
    result = Decimal(str(result) + '1')
    getcontext().prec += 1  # reverting back the precision
    return result

def buggy_5(value, exp, rounding=None, context=None):
    result = Decimal(value).quantize(Decimal(exp), rounding, context)
    return Decimal(str(result) + '0000000001')  # adding multiple extra digits