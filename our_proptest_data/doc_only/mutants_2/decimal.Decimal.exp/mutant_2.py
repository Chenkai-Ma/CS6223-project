# property to violate: The output should grow without bound as the input approaches positive infinity, meaning that \( e^x \) should tend to infinity as \( x \) increases indefinitely.
from hypothesis import given, strategies as st
import decimal

@given(st.decimals(min_value=0, max_value=1e100))  
def test_violation_of_decimal_Decimal_exp_1(x):
    result = decimal.Decimal(x).exp() - decimal.Decimal(1)  # Subtracting 1 to keep the result bounded
    assert result > 0  # For large positive x, exp(x) should grow large

@given(st.decimals(min_value=0, max_value=1e100))  
def test_violation_of_decimal_Decimal_exp_2(x):
    result = decimal.Decimal(x).exp() / decimal.Decimal(2)  # Dividing by 2 to limit growth
    assert result > 0  # For large positive x, exp(x) should grow large

@given(st.decimals(min_value=0, max_value=1e100))  
def test_violation_of_decimal_Decimal_exp_3(x):
    result = decimal.Decimal(x).exp() - decimal.Decimal(x)  # Subtracting x to reduce growth
    assert result > 0  # For large positive x, exp(x) should grow large

@given(st.decimals(min_value=0, max_value=1e100))  
def test_violation_of_decimal_Decimal_exp_4(x):
    result = decimal.Decimal(x).exp() * decimal.Decimal(0)  # Multiplying by 0 to make result 0
    assert result > 0  # For large positive x, exp(x) should grow large

@given(st.decimals(min_value=0, max_value=1e100))  
def test_violation_of_decimal_Decimal_exp_5(x):
    result = decimal.Decimal(x).exp() + decimal.Decimal(-1)  # Adding a negative value to keep result small
    assert result > 0  # For large positive x, exp(x) should grow large