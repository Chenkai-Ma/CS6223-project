# property to violate: If either `self` or `other` is a quiet NaN (n), the function should return the non-NaN operand.
from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=True, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_fma_1(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    if dec_b.is_nan():
        result = dec_a.fma(dec_b, dec_c)
        assert result != dec_a  # Violation: should return dec_a

@given(st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=True, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_fma_2(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    if dec_b.is_nan():
        result = dec_a.fma(dec_b, dec_c)
        assert result != dec_c  # Violation: should return dec_a

@given(st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=True, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_fma_3(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    if dec_b.is_nan():
        result = dec_a.fma(dec_b, dec_c)
        assert result.is_nan()  # Violation: should return dec_a

@given(st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=True, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_fma_4(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    if dec_b.is_nan():
        result = dec_a.fma(dec_b, dec_c)
        assert result == dec_c  # Violation: should return dec_a

@given(st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=True, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_fma_5(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    if dec_b.is_nan():
        result = dec_a.fma(dec_b, dec_c)
        assert result == Decimal('0')  # Violation: should return dec_a