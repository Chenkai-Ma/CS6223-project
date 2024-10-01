import decimal

def buggy_1(self, other, third, context=None):
    result = decimal.Decimal.fma(self, other, third, context)
    return int(result)


def buggy_2(self, other, third, context=None):
    try:
        return decimal.Decimal.fma(self, other, third, context)
    except:
        return None


def buggy_3(self, other, third, context=None):
    third = decimal.Decimal(third)
    return decimal.Decimal.fma(self, other, third, context)


def buggy_4(self, other, third, context=None):
    other = int(other)
    return decimal.Decimal.fma(self, other, third, context)


def buggy_5(self, other, third, context=None):
    result = decimal.Decimal.fma(self, other, third, context)
    return round(result, 2)