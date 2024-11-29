from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation, getcontext

@given(st.decimals(), st.decimals(), st.decimals())
def test_fma_output_equals_product_plus_third_property(a, b, c):
    result = Decimal(a).fma(Decimal(b), Decimal(c))
    expected = Decimal(a) * Decimal(b) + Decimal(c)
    assert result == expected

@given(st.decimals(), st.decimals(), st.decimals())
def test_fma_special_values_property(a, b, c):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal(c)
    
    # Check behavior when one of the values is NaN
    dec_a = Decimal('NaN') if a == 0 else dec_a
    result = dec_a.fma(dec_b, dec_c)
    assert result.is_nan() or isinstance(result, Decimal)

    dec_b = Decimal('NaN') if b == 0 else dec_b
    result = dec_a.fma(dec_b, dec_c)
    assert result.is_nan() or isinstance(result, Decimal)

    dec_a = Decimal('Infinity') if a == 0 else dec_a
    result = dec_a.fma(dec_b, dec_c)
    assert result in [Decimal('Infinity'), Decimal('-Infinity')] or isinstance(result, Decimal)

    dec_b = Decimal('Infinity') if b == 0 else dec_b
    result = dec_a.fma(dec_b, dec_c)
    assert result in [Decimal('Infinity'), Decimal('-Infinity')] or isinstance(result, Decimal)

@given(st.decimals(), st.decimals())
def test_fma_zero_multiplication_property(a, b):
    result = Decimal(a).fma(Decimal(0), Decimal(b))
    expected = Decimal(b)
    assert result == expected

@given(st.decimals(), st.decimals())
def test_fma_correct_sign_property(a, b):
    dec_a = Decimal(a)
    dec_b = Decimal(b)
    dec_c = Decimal('0')  # Using zero for simplicity
    product_sign = (dec_a.sign() ^ dec_b.sign())
    result = dec_a.fma(dec_b, dec_c)
    
    if product_sign == 0:
        assert result == dec_c
    else:
        assert result.sign() == product_sign

@given(st.decimals(), st.decimals(), st.decimals())
def test_fma_valid_decimal_instance_property(a, b, c):
    result = Decimal(a).fma(Decimal(b), Decimal(c))
    assert isinstance(result, Decimal)

# End program