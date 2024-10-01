from decimal import Decimal, getcontext

def buggy_1(value, exp, rounding=None, context=None):
    result = Decimal.quantize(value, exp, rounding, context)
    return result * Decimal('1E999')

def buggy_2(value, exp, rounding=None, context=None):
    result = Decimal.quantize(value, exp, rounding, context)
    return result / Decimal('1E999')

def buggy_3(value, exp, rounding=None, context=None):
    context = getcontext()
    context.Emax = -1
    context.Etiny = 1000
    result = Decimal.quantize(value, exp, rounding, context)
    return result

def buggy_4(value, exp, rounding=None, context=None):
    result = Decimal.quantize(value, exp, rounding, context)
    return Decimal(str(result) + 'E999')

def buggy_5(value, exp, rounding=None, context=None):
    result = Decimal.quantize(value, exp, rounding, context)
    return Decimal(str(result) + 'E-999')