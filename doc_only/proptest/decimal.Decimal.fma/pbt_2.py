from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.decimals(allow_nan=False, allow_infinity=False), 
       st.decimals(allow_nan=False, allow_infinity=False), 
       st.decimals(allow_nan=False, allow_infinity=False))
def test_fma_output_equals_product_plus_third_property(a, b, c):
    result = Decimal(a).fma(Decimal(b), Decimal(c))
    expected = Decimal(a) * Decimal(b) + Decimal(c)
    assert result == expected

@given(st.decimals(allow_nan=False, allow_infinity=False), 
       st.decimals(allow_nan=False, allow_infinity=False), 
       st.decimals(allow_nan=False, allow_infinity=False))
def test_fma_output_is_decimal_property(a, b, c):
    result = Decimal(a).fma(Decimal(b), Decimal(c))
    assert isinstance(result, Decimal)

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_fma_zero_other_property(a):
    result = Decimal(a).fma(Decimal(0), Decimal(5))
    assert result == Decimal(a) + Decimal(5)

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_fma_zero_third_property(a):
    result = Decimal(a).fma(Decimal(3), Decimal(0))
    assert result == Decimal(a) * Decimal(3)

@given(st.decimals(allow_nan=False, allow_infinity=False), 
       st.decimals(allow_nan=False, allow_infinity=False))
def test_fma_commutative_property(b, c):
    a = Decimal(2)  # Fixed value to test commutativity
    result1 = Decimal(a).fma(Decimal(b), Decimal(c))
    result2 = Decimal(a).fma(Decimal(c), Decimal(b))
    assert result1 == result2
# End program