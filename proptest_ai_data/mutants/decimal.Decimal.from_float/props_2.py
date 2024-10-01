import decimal

def buggy_1(f):
  return -decimal.Decimal.from_float(f)

def buggy_2(f):
  return decimal.Decimal.from_float(-abs(f))

def buggy_3(f):
  return decimal.Decimal.from_float(f) * decimal.Decimal('-1')

def buggy_4(f):
  res = decimal.Decimal.from_float(f)
  if res > 0:
    return -res
  return res

def buggy_5(f):
  return decimal.Decimal.from_float(f).copy_negate()