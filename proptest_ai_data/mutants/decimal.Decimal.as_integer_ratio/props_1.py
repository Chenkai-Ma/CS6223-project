import decimal

def buggy_1(self):
    ratio = decimal.Decimal.as_integer_ratio(self)
    return ratio[0]  # Return only the first element from tuple

def buggy_2(self):
    ratio = decimal.Decimal.as_integer_ratio(self)
    return (ratio,'bug')  # Return a tuple where second argument is string not an integer

def buggy_3(self):
    ratio = decimal.Decimal.as_integer_ratio(self)
    return ratio[0],  # Return only first element but in form of a tuple 

def buggy_4(self):
    ratio = decimal.Decimal.as_integer_ratio(self)
    return (ratio[0])  # Return only first element as an integer but in brackets 

def buggy_5(self):
    ratio = decimal.Decimal.as_integer_ratio(self)
    return [ratio[0], ratio[1]]  # Return result as a list not as a tuple