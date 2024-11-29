# property to violate: The output should be equal to the sum of the product of the first two arguments and the third argument, i.e., `self * other + third`.
from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_1(first, second, third):
    result = Decimal(first).fma(second, third) + 1  # Adding 1 to violate the property
    expected = Decimal(first) * Decimal(second) + Decimal(third)
    assert result == expected

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_2(first, second, third):
    result = Decimal(first).fma(second, third) * 2  # Multiplying by 2 to violate the property
    expected = Decimal(first) * Decimal(second) + Decimal(third)
    assert result == expected

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_3(first, second, third):
    result = Decimal(first).fma(second, third) - 100  # Subtracting 100 to violate the property
    expected = Decimal(first) * Decimal(second) + Decimal(third)
    assert result == expected

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_4(first, second, third):
    result = Decimal(first).fma(second, third) + Decimal('0.5')  # Adding 0.5 to violate the property
    expected = Decimal(first) * Decimal(second) + Decimal(third)
    assert result == expected

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_5(first, second, third):
    result = Decimal(first).fma(second, third) - Decimal('1e50')  # Subtracting a large number to violate the property
    expected = Decimal(first) * Decimal(second) + Decimal(third)
    assert result == expected