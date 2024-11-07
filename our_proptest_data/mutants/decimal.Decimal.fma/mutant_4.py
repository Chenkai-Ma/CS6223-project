# property to violate: The output should not be affected by the rounding mode of the context, as the operation is designed to perform the multiplication without rounding the intermediate product.
from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_1(first, third):
    result1 = Decimal(first).fma(third, Decimal(0))
    result2 = Decimal(third).fma(first, Decimal(0)) + Decimal(1)  # Adding 1 to violate the property
    assert result1 == result2

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_2(first, third):
    result1 = Decimal(first).fma(third, Decimal(0))
    result2 = Decimal(third).fma(first, Decimal(0)) * Decimal(2)  # Multiplying by 2 to violate the property
    assert result1 == result2

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_3(first, third):
    result1 = Decimal(first).fma(third, Decimal(0))
    result2 = Decimal(third).fma(first, Decimal(0)) - Decimal(5)  # Subtracting 5 to violate the property
    assert result1 == result2

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_4(first, third):
    result1 = Decimal(first).fma(third, Decimal(0))
    result2 = Decimal(third).fma(first, Decimal(0)).quantize(Decimal('1.0'))  # Quantizing to violate the property
    assert result1 == result2

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_5(first, third):
    result1 = Decimal(first).fma(third, Decimal(0))
    result2 = Decimal(third).fma(first, Decimal(0)).copy_abs()  # Taking absolute value to violate the property
    assert result1 == result2