from decimal import Decimal

def buggy_1(self, other, third, context=None):
    result = Decimal.fma(self, other, third, context)
    if third == 0:
        return result + Decimal('0.1')
    return result


def buggy_2(self, other, third, context=None):
    result = Decimal.fma(self, other, third, context)
    if third == 0:
        return result - Decimal('0.1')
    return result


def buggy_3(self, other, third, context=None):
    result = Decimal.fma(self, other, third, context)
    if third == 0:
        return Decimal('1.0')
    return result


def buggy_4(self, other, third, context=None):
    result = Decimal.fma(self, other, third, context)
    if third == 0:
        return result * Decimal('2')
    return result


def buggy_5(self, other, third, context=None):
    result = Decimal.fma(self, other, third, context)
    if third == 0:
        return result / Decimal('2')
    return result