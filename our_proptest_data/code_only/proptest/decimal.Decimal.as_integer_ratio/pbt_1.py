from hypothesis import given, strategies as st
from decimal import Decimal
import math

@given(st.decimals())
def test_output_is_tuple_property(decimal_value):
    result = decimal_value.as_integer_ratio()
    assert isinstance(result, tuple) and len(result) == 2

@given(st.decimals())
def test_numerator_is_integer_property(decimal_value):
    result = decimal_value.as_integer_ratio()
    numerator, _ = result
    assert isinstance(numerator, int)

@given(st.decimals())
def test_denominator_is_positive_integer_property(decimal_value):
    result = decimal_value.as_integer_ratio()
    _, denominator = result
    assert isinstance(denominator, int) and denominator > 0

@given(st.decimals())
def test_fraction_equals_original_decimal_property(decimal_value):
    result = decimal_value.as_integer_ratio()
    numerator, denominator = result
    assert Decimal(numerator) / Decimal(denominator) == decimal_value

@given(st.decimals())
def test_gcd_is_one_property(decimal_value):
    result = decimal_value.as_integer_ratio()
    numerator, denominator = result
    assert math.gcd(numerator, denominator) == 1
# End program