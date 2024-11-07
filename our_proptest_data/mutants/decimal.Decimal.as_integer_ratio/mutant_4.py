# property to violate: If the input Decimal is a finite number, the output pair (n, d) must represent the exact value of the Decimal as a fraction.
from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_as_integer_ratio_1(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    # Modify the output to violate the property by changing n
    assert Decimal(n + 1) / Decimal(d) == decimal_value

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_as_integer_ratio_2(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    # Modify the output to violate the property by changing d
    assert Decimal(n) / Decimal(d + 1) == decimal_value

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_as_integer_ratio_3(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    # Modify the output to violate the property by changing both n and d
    assert Decimal(n + 2) / Decimal(d + 2) == decimal_value

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_as_integer_ratio_4(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    # Modify the output to violate the property by using a constant instead of n
    assert Decimal(1) / Decimal(d) == decimal_value

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_as_integer_ratio_5(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    # Modify the output to violate the property by using a constant instead of d
    assert Decimal(n) / Decimal(1) == decimal_value