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
        assert result == dec_c  # Violating the property by returning dec_c instead of dec_a

@given(st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=True, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_fma_2(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    if dec_b.is_nan():
        result = dec_a.fma(dec_b, dec_c)
        assert result == Decimal('0')  # Violating the property by returning a constant value

@given(st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=True, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_fma_3(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    if dec_b.is_nan():
        result = dec_a.fma(dec_b, dec_c)
        assert result == dec_b  # Violating the property by returning dec_b instead of dec_a

@given(st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=True, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_fma_4(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    if dec_b.is_nan():
        result = dec_a.fma(dec_b, dec_c)
        assert result == Decimal('NaN')  # Violating the property by returning NaN

@given(st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=True, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_fma_5(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    if dec_b.is_nan():
        result = dec_a.fma(dec_b, dec_c)
        assert result == dec_a + dec_c  # Violating the property by performing an operation instead of returning dec_a