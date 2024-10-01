from decimal import Decimal

def buggy_1(f):
    result = Decimal.from_float(f)
    if str(result) == 'NaN':
        return Decimal('Infinity')
    elif str(result) == 'Infinity':
        return Decimal('-Infinity')
    elif str(result) == '-Infinity':
        return Decimal('NaN')
    else:
        return result

def buggy_2(f):
    result = Decimal.from_float(f)
    if str(result) == 'NaN':
        return Decimal('-Infinity')
    elif str(result) == 'Infinity':
        return Decimal('NaN')
    elif str(result) == '-Infinity':
        return Decimal('Infinity')
    else:
        return result

def buggy_3(f):
    result = Decimal.from_float(f)
    if str(result) == 'NaN':
        return Decimal('1')
    elif str(result) == 'Infinity':
        return Decimal('2')
    elif str(result) == '-Infinity':
        return Decimal('3')
    else:
        return result

def buggy_4(f):
    result = Decimal.from_float(f)
    if str(result) == 'NaN':
        return Decimal('0')
    elif str(result) == 'Infinity':
        return Decimal('1')
    elif str(result) == '-Infinity':
        return Decimal('-1')
    else:
        return result

def buggy_5(f):
    result = Decimal.from_float(f)
    if str(result) == 'NaN':
        return Decimal('Infinity').copy_negate()
    elif str(result) == 'Infinity':
        return Decimal('NaN').copy_sign(Decimal('1'))
    elif str(result) == '-Infinity':
        return Decimal('NaN').copy_sign(Decimal('-1'))
    else:
        return result