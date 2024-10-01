import decimal
from fractions import Fraction

def buggy_1(decimal_instance):
    n, d = decimal_instance.as_integer_ratio()
    return n * 2, d  # both numerator and denominator multiplied by 2

def buggy_2(decimal_instance):
    n, d = decimal_instance.as_integer_ratio()
    return n, d * 2  # just denominator multipled by 2

def buggy_3(decimal_instance):
    n, d = decimal_instance.as_integer_ratio()
    if n != 0:
        n += 1   # increment numerator by one
    return n, d

def buggy_4(decimal_instance):
    n, d = decimal_instance.as_integer_ratio()
    if d != 0:
        d += 1   # increment denominator by one
    return n, d

def buggy_5(decimal_instance):
    n, d = decimal_instance.as_integer_ratio()
    frac = Fraction(n, d)
    if frac.numerator != n or frac.denominator != d:
        return n, d * 2   # if lowest terms are not achieved then make it worse
    else:
        return n * 2, d   # if already in lowest terms, violate it