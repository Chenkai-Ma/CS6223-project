from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation, getcontext

@given(st.floats(min_value=-1e100, max_value=1e100), 
       st.floats(min_value=-1e100, max_value=1e100), 
       st.floats(min_value=-1e100, max_value=1e100))
def test_decimal_Decimal_fma_basic_arithmetic_property(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    if not dec_a.is_nan() and not dec_b.is_nan():
        assert dec_a.fma(dec_b, dec_c) == dec_a * dec_b + dec_c

@given(st.decimals(allow_nan=False, allow_infinity=False), 
       st.decimals(allow_nan=False, allow_infinity=False), 
       st.decimals())
def test_decimal_Decimal_fma_signaling_nan_property(dec_a, dec_b, dec_c):
    dec_a = Decimal(dec_a)
    dec_b = Decimal(dec_b)
    if dec_a.is_nan() or dec_b.is_nan():
        with st.raises(InvalidOperation):
            dec_a.fma(dec_b, dec_c)

@given(st.decimals(allow_nan=False, allow_infinity=False), 
       st.decimals())
def test_decimal_Decimal_fma_quiet_nan_property(dec_a, dec_c):
    dec_a = Decimal(dec_a)
    if dec_a.is_nan():
        result = dec_a.fma(Decimal('1.0'), dec_c)
        assert result == dec_a

@given(st.decimals(allow_nan=False), 
       st.decimals())
def test_decimal_Decimal_fma_infinity_property(dec_a, dec_c):
    dec_a = Decimal(dec_a)
    if dec_a.is_infinite():
        with st.raises(InvalidOperation):
            dec_a.fma(Decimal('0'), dec_c)

@given(st.decimals(allow_nan=False, allow_infinity=False), 
       st.decimals(allow_nan=False, allow_infinity=False), 
       st.decimals())
def test_decimal_Decimal_fma_sign_property(dec_a, dec_b, dec_c):
    dec_a = Decimal(dec_a)
    dec_b = Decimal(dec_b)
    dec_c = Decimal(dec_c)
    if not dec_a.is_zero() and not dec_b.is_zero():
        sign_product = (dec_a.sign() ^ dec_b.sign())
        result = dec_a.fma(dec_b, dec_c)
        assert result.sign() == sign_product

# End program