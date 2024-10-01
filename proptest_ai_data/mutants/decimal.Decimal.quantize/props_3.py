import decimal
from decimal import Decimal

def buggy_1(value, exp, rounding=None, context=None):
    try:
        result = Decimal(value).quantize(Decimal(exp), rounding, context)
        if result==0 and value!=exp:
            raise decimal.Underflow('Underflow error')
        return result
    except decimal.InvalidOperation:
        raise

def buggy_2(value, exp, rounding=None, context=None):
    try:
        result = Decimal(value).quantize(Decimal(exp), rounding, context)
        if result<1 and value>1:
            raise decimal.Underflow('Underflow error')
        return result
    except decimal.InvalidOperation:
        raise

def buggy_3(value, exp, rounding=None, context=None):
    try:
        result = Decimal(value).quantize(Decimal(exp), rounding, context)
        if result>0 and result<1:
            raise decimal.Underflow('Underflow error')
        return result
    except decimal.InvalidOperation:
        raise

def buggy_4(value, exp, rounding=None, context=None):
    try:
        result = Decimal(value).quantize(Decimal(exp), rounding, context)
        if value!=exp and abs(value-exp) > decimal.getcontext().Emax:
            raise decimal.Underflow('Underflow error')
        return result
    except decimal.InvalidOperation:
        raise

def buggy_5(value, exp, rounding=None, context=None):
    try:
        result = Decimal(value).quantize(Decimal(exp), rounding, context)
        if abs(value-exp) > decimal.getcontext().prec:
            raise decimal.Underflow('Underflow error')
        return result
    except decimal.InvalidOperation:
        raise