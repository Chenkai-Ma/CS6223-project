from hypothesis import given, strategies as st
from decimal import Decimal
from math import gcd

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_as_integer_ratio_tuple_length_property(value):
    numerator, denominator = value.as_integer_ratio()
    assert isinstance(numerator, int)
    assert isinstance(denominator, int)
    assert len((numerator, denominator)) == 2

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_as_integer_ratio_numerator_property(value):
    numerator, denominator = value.as_integer_ratio()
    assert isinstance(numerator, int)

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_as_integer_ratio_denominator_property(value):
    numerator, denominator = value.as_integer_ratio()
    assert isinstance(denominator, int)
    assert denominator > 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_as_integer_ratio_equivalence_property(value):
    numerator, denominator = value.as_integer_ratio()
    assert numerator / denominator == value

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_as_integer_ratio_simplest_form_property(value):
    numerator, denominator = value.as_integer_ratio()
    assert gcd(numerator, denominator) == 1
# End program