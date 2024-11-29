# property to violate: The result of `fma(self, other, third)` should be equal to `self * other + third` when neither `self` nor `other` are special values (like NaN or Infinity).
from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_fma_1(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    result = dec_a.fma(dec_b, dec_c) + 1  # Adding 1 to the result to violate the property
    expected = dec_a * dec_b + dec_c
    assert result == expected

@given(st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_fma_2(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    result = dec_a.fma(dec_b, dec_c) * 2  # Multiplying the result by 2 to violate the property
    expected = dec_a * dec_b + dec_c
    assert result == expected

@given(st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_fma_3(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    result = dec_a.fma(dec_b, dec_c) - dec_c  # Subtracting dec_c from the result to violate the property
    expected = dec_a * dec_b + dec_c
    assert result == expected

@given(st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_fma_4(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    result = dec_a.fma(dec_b, dec_c) + dec_a * dec_b  # Adding dec_a * dec_b to the result to violate the property
    expected = dec_a * dec_b + dec_c
    assert result == expected

@given(st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_fma_5(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    result = dec_a.fma(dec_b, dec_c) / 2  # Dividing the result by 2 to violate the property
    expected = dec_a * dec_b + dec_c
    assert result == expected