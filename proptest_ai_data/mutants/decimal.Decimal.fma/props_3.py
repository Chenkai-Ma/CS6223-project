from decimal import Decimal

# Buggy version 1: Simply switch the 'other' and 'third' parameters
def buggy_1(self, other, third, context=None):
    return Decimal.fma(self, third, other, context)

# Buggy version 2: Return result subtracted by third
def buggy_2(self, other, third, context=None):
    res = Decimal.fma(self, other, third, context)
    return res - Decimal(third)

# Buggy version 3: Multiply result by 2
def buggy_3(self, other, third, context=None):
    res = Decimal.fma(self, other, third, context)
    return res * 2

# Buggy version 4: Always return the 'third' parameter
def buggy_4(self, other, third, context=None):
    return Decimal(third)

# Buggy version 5: Return the square of the result
def buggy_5(self, other, third, context=None):
    res = Decimal.fma(self, other, third, context)
    return res ** 2