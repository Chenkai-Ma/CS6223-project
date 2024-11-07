from hypothesis import given, strategies as st
from decimal import Decimal
import math

@given(st.decimals())
def test_as_integer_ratio_output_is_tuple_property(decimal_value):
    result = decimal_value.as_integer_ratio()
    assert isinstance(result, tuple) and len(result) == 2

@given(st.decimals())
def test_as_integer_ratio_numerator_is_integer_property(decimal_value):
    numerator, denominator = decimal_value.as_integer_ratio()
    assert isinstance(numerator, int)

@given(st.decimals())
def test_as_integer_ratio_denominator_is_positive_property(decimal_value):
    numerator, denominator = decimal_value.as_integer_ratio()
    assert denominator > 0

@given(st.decimals())
def test_as_integer_ratio_fraction_equals_decimal_property(decimal_value):
    numerator, denominator = decimal_value.as_integer_ratio()
    assert Decimal(numerator) / Decimal(denominator) == decimal_value

@given(st.decimals())
def test_as_integer_ratio_gcd_is_one_property(decimal_value):
    numerator, denominator = decimal_value.as_integer_ratio()
    assert math.gcd(numerator, denominator) == 1
# End program