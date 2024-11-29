# property to violate: The denominator d must always be positive, regardless of the input Decimal value.
from hypothesis import given, strategies as st
import decimal

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_as_integer_ratio_1(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    d = -abs(d)  # Force the denominator to be negative
    assert d > 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_as_integer_ratio_2(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    d = -1  # Set the denominator to a negative constant
    assert d > 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_as_integer_ratio_3(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    d = n * -1  # Make the denominator negative based on the numerator
    assert d > 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_as_integer_ratio_4(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    d = -d  # Invert the sign of the denominator
    assert d > 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_as_integer_ratio_5(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    d = -100  # Set the denominator to a fixed negative value
    assert d > 0