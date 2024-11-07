# property to violate: The output should grow without bound as the input approaches positive infinity, meaning that \( e^x \) should tend to infinity as \( x \) increases indefinitely.
from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.decimals(min_value=0, max_value=1e100))  # Limiting to avoid overflow
def test_violation_of_decimal_Decimal_exp_1(x):
    result = Decimal(x).exp()
    assert result < 1  # For large positive x, exp(x) should not be less than 1

@given(st.decimals(min_value=0, max_value=1e100))  # Limiting to avoid overflow
def test_violation_of_decimal_Decimal_exp_2(x):
    result = Decimal(x).exp()
    assert result == 1  # For large positive x, exp(x) should not equal 1

@given(st.decimals(min_value=0, max_value=1e100))  # Limiting to avoid overflow
def test_violation_of_decimal_Decimal_exp_3(x):
    result = Decimal(x).exp()
    assert result < Decimal('2.718281828459045235360287471')  # For large positive x, exp(x) should exceed this value

@given(st.decimals(min_value=0, max_value=1e100))  # Limiting to avoid overflow
def test_violation_of_decimal_Decimal_exp_4(x):
    result = Decimal(x).exp()
    assert result == 0  # For large positive x, exp(x) should not equal 0

@given(st.decimals(min_value=0, max_value=1e100))  # Limiting to avoid overflow
def test_violation_of_decimal_Decimal_exp_5(x):
    result = Decimal(x).exp()
    assert result < Decimal(x)  # For large positive x, exp(x) should not be less than x