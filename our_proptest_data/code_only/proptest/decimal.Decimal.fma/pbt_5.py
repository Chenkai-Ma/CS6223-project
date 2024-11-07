from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation, getcontext

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_decimal_Decimal_fma_commutative_property(a, b, c):
    result = a.fma(b, c)
    expected = a * b + c
    assert result == expected

@given(st.decimals(), st.decimals(), st.decimals())
def test_decimal_Decimal_fma_sNaN_property(a, b, c):
    if a.is_nan() or b.is_nan():
        with pytest.raises(InvalidOperation):
            a.fma(b, c)
    else:
        a.fma(b, c)  # No exception should be raised

@given(st.decimals(), st.decimals(), st.decimals())
def test_decimal_Decimal_fma_n_property(a, b, c):
    if a.is_nan() or b.is_nan():
        result = a.fma(b, c)
        assert result == (b if a.is_nan() else a)
    else:
        a.fma(b, c)  # No special condition should alter the result

@given(st.decimals(), st.decimals(), st.decimals())
def test_decimal_Decimal_fma_infinity_property(a, b, c):
    if a.is_infinite() or b.is_infinite():
        if a.is_zero() and b.is_infinite():
            with pytest.raises(InvalidOperation):
                a.fma(b, c)
        elif b.is_zero() and a.is_infinite():
            with pytest.raises(InvalidOperation):
                a.fma(b, c)
        else:
            result = a.fma(b, c)
            # Check if the result is still infinity or the expected value
            assert result.is_infinite() or result == (a * b + c)

@given(st.decimals(), st.decimals(), st.decimals())
def test_decimal_Decimal_fma_sign_property(a, b, c):
    if a.is_finite() and b.is_finite() and a != 0 and b != 0:
        result = a.fma(b, c)
        sign_product = (a.sign() ^ b.sign())
        expected_sign = sign_product if (c.is_zero() or c.is_finite()) else None  # Adjust for c being zero
        assert result.sign() == expected_sign

# End program