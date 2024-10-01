# Buggy version 1: changes the output to an integer
def buggy_1(self, other, third, context=None):
    return int(decimal.Decimal.fma(self, other, third, context))

# Buggy version 2: changes the output to a float
def buggy_2(self, other, third, context=None):
    return float(decimal.Decimal.fma(self, other, third, context))

# Buggy version 3: changes the output to a string
def buggy_3(self, other, third, context=None):
    return str(decimal.Decimal.fma(self, other, third, context))

# Buggy version 4: changes the output to a boolean. If result is 0, return False, otherwise return True
def buggy_4(self, other, third, context=None):
    return bool(decimal.Decimal.fma(self, other, third, context))

# Buggy version 5: changes the output to a list with the output as its only element
def buggy_5(self, other, third, context=None):
    return [decimal.Decimal.fma(self, other, third, context)]