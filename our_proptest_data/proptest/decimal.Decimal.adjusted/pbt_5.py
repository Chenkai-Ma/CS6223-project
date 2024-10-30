from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_adjusted_exponent_minimum_property(decimal_value):
    if decimal_value != 0:
        adjusted_value = decimal_value.adjusted()
        assert adjusted_value >= decimal_value.as_tuple().exponent

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_adjusted_exponent_maximum_property(decimal_value):
    if decimal_value != 0:
        adjusted_value = decimal_value.adjusted()
        assert adjusted_value <= decimal_value.as_tuple().exponent + len(decimal_value.as_tuple().digits) - 1

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_adjusted_exponent_zero_property(decimal_value):
    if decimal_value == 0:
        assert decimal_value.adjusted() == float('-inf')

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_adjusted_exponent_digit_count_property(decimal_value):
    if decimal_value != 0:
        adjusted_value = decimal_value.adjusted()
        digit_count = len(decimal_value.as_tuple().digits)
        assert adjusted_value == digit_count - 1

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_adjusted_exponent_invariance_property(decimal_value):
    if decimal_value != 0:
        representation_1 = Decimal(str(decimal_value))
        representation_2 = Decimal(representation_1.to_eng_string())
        assert representation_1.adjusted() == representation_2.adjusted()
# End program