from decimal import Decimal

# Buggy Function 1
def buggy_1(other, third, context=None):
    return Decimal(1).fma(other, third, context)

# Buggy Function 2
def buggy_2(self, other, context=None):
    return self.fma(other, 1, context)

# Buggy Function 3
def buggy_3(self, third, context=None):
    return self.fma(1, third, context)

# Buggy Function 4
def buggy_4(self, other, third):
    return self.fma(other, third, 1)

# Buggy Function 5
def buggy_5(self, other, third, context=None):
    if (other==None):
        other=1
    if (third==None):
        third=1
    return self.fma(other, third, context)