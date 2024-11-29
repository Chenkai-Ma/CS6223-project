from hypothesis import given, strategies as st
from decimal import Decimal
import math

@given(st.data())
def test_as_integer_ratio_output_structure_property(data):
    decimal_value = data.draw(st.decimals(allow_nan=False, allow_infinity=False))
    numerator, denominator = decimal_value.as_integer_ratio()
    assert isinstance(numerator, int)
    assert isinstance(denominator, int)

@given(st.data())
def test_as_integer_ratio_numerator_property(data):
    decimal_value = data.draw(st.decimals(allow_nan=False, allow_infinity=False))
    numerator, denominator = decimal_value.as_integer_ratio()
    assert isinstance(numerator, int)

@given(st.data())
def test_as_integer_ratio_denominator_property(data):
    decimal_value = data.draw(st.decimals(allow_nan=False, allow_infinity=False))
    numerator, denominator = decimal_value.as_integer_ratio()
    assert denominator > 0

@given(st.data())
def test_as_integer_ratio_equivalence_property(data):
    decimal_value = data.draw(st.decimals(allow_nan=False, allow_infinity=False))
    numerator, denominator = decimal_value.as_integer_ratio()
    assert Decimal(numerator) / Decimal(denominator) == decimal_value

@given(st.data())
def test_as_integer_ratio_simplest_form_property(data):
    decimal_value = data.draw(st.decimals(allow_nan=False, allow_infinity=False))
    numerator, denominator = decimal_value.as_integer_ratio()
    assert math.gcd(numerator, denominator) == 1
# End program