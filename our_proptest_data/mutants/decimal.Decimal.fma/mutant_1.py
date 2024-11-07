# property to violate: The output should be equal to the sum of the product of the first two arguments and the third argument, i.e., `self * other + third`.
from hypothesis import given, strategies as st
import decimal

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_1(first, second, third):
    result = decimal.Decimal(first).fma(second, third)
    expected = decimal.Decimal(first) * decimal.Decimal(second) + decimal.Decimal(third) + 1  # Adding 1 to violate the property
    assert result == expected

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_2(first, second, third):
    result = decimal.Decimal(first).fma(second, third)
    expected = decimal.Decimal(first) * decimal.Decimal(second) + decimal.Decimal(third) - 1  # Subtracting 1 to violate the property
    assert result == expected

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_3(first, second, third):
    result = decimal.Decimal(first).fma(second, third)
    expected = decimal.Decimal(first) * decimal.Decimal(second) + decimal.Decimal(third) * 2  # Doubling the third argument to violate the property
    assert result == expected

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_4(first, second, third):
    result = decimal.Decimal(first).fma(second, third)
    expected = decimal.Decimal(first) * decimal.Decimal(second) + decimal.Decimal(third) + decimal.Decimal(first)  # Adding first argument to violate the property
    assert result == expected

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_5(first, second, third):
    result = decimal.Decimal(first).fma(second, third)
    expected = decimal.Decimal(first) * decimal.Decimal(second) + decimal.Decimal(third) / 2  # Halving the third argument to violate the property
    assert result == expected