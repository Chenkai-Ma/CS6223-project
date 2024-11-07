from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation, getcontext

# Adjust the precision context to handle large numbers
getcontext().prec = 50

@given(st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_fma_basic_property(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    result = dec_a.fma(dec_b, dec_c)
    expected = dec_a * dec_b + dec_c
    assert result == expected

@given(st.floats(allow_nan=True, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_fma_sNaN_property(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    if dec_a.is_nan():
        try:
            dec_a.fma(dec_b, dec_c)
            assert False, "Expected InvalidOperation for sNaN"
        except InvalidOperation:
            pass

@given(st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=True, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_fma_nNaN_property(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    if dec_b.is_nan():
        result = dec_a.fma(dec_b, dec_c)
        assert result == dec_a

@given(st.floats(allow_nan=False, allow_infinity=True), 
       st.floats(allow_nan=False, allow_infinity=True), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_fma_infinity_property(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    if dec_a.is_infinite() or dec_b.is_infinite():
        try:
            result = dec_a.fma(dec_b, dec_c)
            if dec_a.is_zero() or dec_b.is_zero():
                assert False, "Expected InvalidOperation for INF * 0"
        except InvalidOperation:
            pass

@given(st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False), 
       st.floats(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_fma_sign_property(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    if dec_a != 0 and dec_b != 0:
        result = dec_a.fma(dec_b, dec_c)
        expected_sign = (dec_a.sign() ^ dec_b.sign())
        assert result.sign() == expected_sign

# End program