def buggy_1(dec):
   n, d = decimal.Decimal.as_integer_ratio(dec)
   return -n, -d 

def buggy_2(dec):
   n, d = decimal.Decimal.as_integer_ratio(dec)
   return n, -d 

def buggy_3(dec):
   n, d = decimal.Decimal.as_integer_ratio(dec)
   return -n, d

def buggy_4(dec):
   n, d = decimal.Decimal.as_integer_ratio(dec)
   if n < 0:
       n = abs(n)
   d = -d
   return n, d

def buggy_5(dec):
    n, d = decimal.Decimal.as_integer_ratio(dec)
    return d, n