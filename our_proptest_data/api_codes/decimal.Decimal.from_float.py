@classmethod
def from_float(cls, f):
    if isinstance(f, int):                # handle integer inputs
        sign = 0 if f >= 0 else 1
        k = 0
        coeff = str(abs(f))
    elif isinstance(f, float):
        if _math.isinf(f) or _math.isnan(f):
            return cls(repr(f))
        if _math.copysign(1.0, f) == 1.0:
            sign = 0
        else:
            sign = 1
        n, d = abs(f).as_integer_ratio()
        k = d.bit_length() - 1
        coeff = str(n*5**k)
    else:
        raise TypeError("argument must be int or float.")

    result = _dec_from_triple(sign, coeff, -k)
    if cls is Decimal:
        return result
    else:
        return cls(result)