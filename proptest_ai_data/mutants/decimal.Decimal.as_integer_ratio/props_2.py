from decimal import Decimal

def buggy_1(number):
    n, d = Decimal(number).as_integer_ratio()
    return n + 0.5, d  # n is not an integer

def buggy_2(number):
    n, d = Decimal(number).as_integer_ratio()
    return n, d + 0.3  # d is not an integer

def buggy_3(number):
    n, d = Decimal(number).as_integer_ratio()
    return str(n), d  # n is not an integer, it's a string

def buggy_4(number):
    n, d = Decimal(number).as_integer_ratio()
    return n, str(d)  # d is not an integer, it's a string

def buggy_5(number):
    n, d = Decimal(number).as_integer_ratio()
    return [n], [d]  # n & d are not integers, they're lists