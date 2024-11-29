from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_output_is_integer_property(d):
    result = d.adjusted()
    assert isinstance(result, int)

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_zero_coefficient_returns_zero_property(d):
    if d == Decimal(0):
        result = d.adjusted()
        assert result == 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_output_greater_than_or_equal_to_exponent_property(d):
    if d != Decimal(0):
        result = d.adjusted()
        assert result >= d.as_tuple().exponent

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_adjusted_correctly_accounts_for_scientific_notation_property(d):
    if d != Decimal(0):
        result = d.adjusted()
        lead_digit_position = len(d.as_tuple().digits) - 1
        assert result == d.exponent + lead_digit_position

@given(st.decimals(allow_nan=True, allow_infinity=True))
def test_nan_or_infinity_returns_zero_property(d):
    if d.is_nan() or d.is_infinite():
        result = d.adjusted()
        assert result == 0
# End program