from hypothesis import given, strategies as st
from decimal import Decimal
import math

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_as_integer_ratio_output_structure_property(decimal_value):
    numerator, denominator = decimal_value.as_integer_ratio()
    assert isinstance(numerator, int)
    assert isinstance(denominator, int)

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_as_integer_ratio_denominator_positive_property(decimal_value):
    numerator, denominator = decimal_value.as_integer_ratio()
    assert denominator > 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_as_integer_ratio_equivalence_property(decimal_value):
    numerator, denominator = decimal_value.as_integer_ratio()
    assert Decimal(numerator) / Decimal(denominator) == decimal_value

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_as_integer_ratio_gcd_one_property(decimal_value):
    numerator, denominator = decimal_value.as_integer_ratio()
    assert math.gcd(numerator, denominator) == 1

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_as_integer_ratio_output_tuple_length_property(decimal_value):
    result = decimal_value.as_integer_ratio()
    assert len(result) == 2
# End program