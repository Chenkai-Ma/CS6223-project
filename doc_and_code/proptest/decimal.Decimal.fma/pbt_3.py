from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation, getcontext

@given(st.decimals(), st.decimals(), st.decimals())
def test_fma_output_equals_product_plus_third_property(a, b, c):
    result = Decimal(a).fma(Decimal(b), Decimal(c))
    expected = Decimal(a) * Decimal(b) + Decimal(c)
    assert result == expected

@given(st.decimals(), st.decimals())
def test_fma_special_values_property(a, b):
    a_decimal = Decimal(a)
    b_decimal = Decimal(b)
    
    if a_decimal.is_nan() or b_decimal.is_nan():
        with pytest.raises(InvalidOperation):
            a_decimal.fma(b_decimal, Decimal(0))
    elif a_decimal.is_infinite() or b_decimal.is_infinite():
        if a_decimal.is_infinite() and b_decimal.is_zero():
            with pytest.raises(InvalidOperation):
                a_decimal.fma(b_decimal, Decimal(0))
        elif b_decimal.is_infinite() and a_decimal.is_zero():
            with pytest.raises(InvalidOperation):
                a_decimal.fma(b_decimal, Decimal(0))

@given(st.decimals(), st.decimals())
def test_fma_sign_property(a, b):
    a_decimal = Decimal(a)
    b_decimal = Decimal(b)
    third = Decimal(0)  # Using zero to isolate the product behavior
    
    result = a_decimal.fma(b_decimal, third)
    expected_sign = (a_decimal.sign() ^ b_decimal.sign())
    
    if expected_sign == 0:  # Both are positive
        assert result >= 0
    else:  # One is negative
        assert result < 0

@given(st.decimals(), st.decimals())
def test_fma_zero_multiplication_property(a, b):
    a_decimal = Decimal(a)
    b_decimal = Decimal(b)
    third = Decimal(5)  # Non-zero value for third
    
    result = a_decimal.fma(Decimal(0), third)
    assert result == third

@given(st.decimals(), st.decimals(), st.decimals())
def test_fma_output_type_property(a, b, c):
    result = Decimal(a).fma(Decimal(b), Decimal(c))
    assert isinstance(result, Decimal)

# End program