# property to violate: The denominator returned by `as_integer_ratio` should be a positive integer.
from hypothesis import given, strategies as st
import decimal
from decimal import Decimal

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_as_integer_ratio_1(decimal_value):
    numerator, denominator = decimal_value.as_integer_ratio()
    # Force the denominator to be negative
    denominator = -denominator
    assert Decimal(numerator) / Decimal(denominator) == decimal_value

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_as_integer_ratio_2(decimal_value):
    numerator, denominator = decimal_value.as_integer_ratio()
    # Set the denominator to zero
    denominator = 0
    assert Decimal(numerator) / Decimal(denominator) == decimal_value

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_as_integer_ratio_3(decimal_value):
    numerator, denominator = decimal_value.as_integer_ratio()
    # Change the denominator to a negative number
    denominator = -1
    assert Decimal(numerator) / Decimal(denominator) == decimal_value

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_as_integer_ratio_4(decimal_value):
    numerator, denominator = decimal_value.as_integer_ratio()
    # Make the denominator a large negative integer
    denominator = -1000000
    assert Decimal(numerator) / Decimal(denominator) == decimal_value

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_as_integer_ratio_5(decimal_value):
    numerator, denominator = decimal_value.as_integer_ratio()
    # Set the denominator to a negative power of ten
    denominator = -10
    assert Decimal(numerator) / Decimal(denominator) == decimal_value