from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation, getcontext

@given(st.decimals(), st.decimals(), st.decimals())
def test_decimal_Decimal_fma_property_non_special_values(a, b, c):
    if a.is_nan() or b.is_nan() or a.is_infinite() or b.is_infinite():
        return  # Skip if any operand is NaN or Infinity
    result = a.fma(b, c)
    expected = a * b + c
    assert result == expected

@given(st.decimals())
def test_decimal_Decimal_fma_property_signaling_nan(a):
    context = getcontext()
    context.traps[InvalidOperation] = True  # Enable trapping for NaN
    s_nan = Decimal('sNaN')
    with st.raises(InvalidOperation):
        a.fma(s_nan, Decimal('1'), Decimal('1'))

@given(st.decimals())
def test_decimal_Decimal_fma_property_quiet_nan(a):
    n_nan = Decimal('n')
    result = a.fma(n_nan, Decimal('1'))
    assert result == a

@given(st.decimals())
def test_decimal_Decimal_fma_property_infinity(a):
    inf = Decimal('Infinity')
    if a.is_zero():
        with st.raises(InvalidOperation):
            a.fma(inf, Decimal('1'), Decimal('1'))
    else:
        result = a.fma(inf, Decimal('1'), Decimal('1'))
        assert result == inf  # Result should be Infinity

@given(st.decimals(), st.decimals(), st.decimals())
def test_decimal_Decimal_fma_property_sign_adjustment(a, b, c):
    if a.is_nan() or b.is_nan() or a.is_infinite() or b.is_infinite():
        return  # Skip if any operand is NaN or Infinity
    result = a.fma(b, c)
    product_sign = (a.sign() ^ b.sign())
    assert result.sign() == product_sign  # Check if the sign is maintained

# End program