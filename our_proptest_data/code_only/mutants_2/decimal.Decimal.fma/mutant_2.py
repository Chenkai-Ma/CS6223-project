# property to violate: If either `self` or `other` is a signaling NaN (sNaN), the function should raise an `InvalidOperation` error.
from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation

@given(st.floats(allow_nan=True, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_fma_1(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    if dec_a.is_nan():
        # Modify the output to not raise an error
        result = dec_a.fma(dec_b, dec_c)
        assert result is not None, "Expected a valid result"

@given(st.floats(allow_nan=True, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_fma_2(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    if dec_a.is_nan():
        # Modify the output to not raise an error
        result = dec_a.fma(dec_b, dec_c)
        assert result == 0, "Expected a result of 0"

@given(st.floats(allow_nan=True, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_fma_3(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    if dec_a.is_nan():
        # Modify the output to not raise an error
        result = dec_a.fma(dec_b, dec_c)
        assert result == 1, "Expected a result of 1"

@given(st.floats(allow_nan=True, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_fma_4(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    if dec_a.is_nan():
        # Modify the output to not raise an error
        result = dec_a.fma(dec_b, dec_c)
        assert result == -1, "Expected a result of -1"

@given(st.floats(allow_nan=True, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_fma_5(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    if dec_a.is_nan():
        # Modify the output to not raise an error
        result = dec_a.fma(dec_b, dec_c)
        assert result == float('inf'), "Expected a result of infinity"