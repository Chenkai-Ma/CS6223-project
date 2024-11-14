from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.decimals())
def test_output_is_integer_property(decimal_value):
    assert isinstance(decimal_value.adjusted(), int)

@given(st.decimals(min_value=Decimal('0'), max_value=Decimal('1e+100')))
def test_zero_coefficient_returns_zero_property(decimal_value):
    if decimal_value == Decimal('0'):
        assert decimal_value.adjusted() == 0

@given(st.decimals())
def test_output_greater_than_or_equal_to_exponent_property(decimal_value):
    if decimal_value != Decimal('0'):
        assert decimal_value.adjusted() >= decimal_value._exp

@given(st.decimals())
def test_scientific_notation_correctness_property(decimal_value):
    if decimal_value != Decimal('0'):
        lead_digit_position = len(decimal_value._int) - 1
        assert decimal_value.adjusted() == decimal_value._exp + lead_digit_position

@given(st.one_of(st.decimals(negative=True), st.decimals(positive=True)).filter(lambda x: x.is_nan() or x.is_infinite()))
def test_nan_or_infinity_returns_zero_property(decimal_value):
    if decimal_value.is_nan() or decimal_value.is_infinite():
        assert decimal_value.adjusted() == 0
# End program