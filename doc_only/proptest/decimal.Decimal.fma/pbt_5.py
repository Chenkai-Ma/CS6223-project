from hypothesis import given, strategies as st
from decimal import Decimal, getcontext

# Set a high precision to handle large numbers
getcontext().prec = 100

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_output_equals_product_plus_third_property(first, second, third):
    result = Decimal(first).fma(second, third)
    expected = Decimal(first) * Decimal(second) + Decimal(third)
    assert result == expected

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_output_is_decimal_type_property(first, second):
    result = Decimal(first).fma(second, Decimal(0))
    assert isinstance(result, Decimal)

@given(st.decimals(min_value=-1e100, max_value=1e100))
def test_output_with_zero_other_property(first):
    result = Decimal(first).fma(Decimal(0), Decimal(5))
    expected = Decimal(first) + Decimal(5)
    assert result == expected

@given(st.decimals(min_value=-1e100, max_value=1e100))
def test_output_with_zero_third_property(first):
    result = Decimal(first).fma(Decimal(3), Decimal(0))
    expected = Decimal(first) * Decimal(3)
    assert result == expected

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_commutative_property_of_addition(first, third):
    result1 = Decimal(first).fma(third, Decimal(0))
    result2 = Decimal(third).fma(first, Decimal(0))
    assert result1 == result2
# End program