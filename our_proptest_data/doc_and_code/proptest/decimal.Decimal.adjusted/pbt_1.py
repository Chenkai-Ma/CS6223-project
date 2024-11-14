from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_adjusted_output_integer_property(decimal_value):
    result = decimal_value.adjusted()
    assert isinstance(result, int)

@given(st.decimals(allow_nan=False, allow_infinity=False).filter(lambda d: d == 0))
def test_decimal_Decimal_adjusted_zero_coefficient_property(decimal_value):
    result = decimal_value.adjusted()
    assert result == 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_adjusted_exponent_non_zero_property(decimal_value):
    if decimal_value != 0:
        result = decimal_value.adjusted()
        assert result >= decimal_value._exp

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_adjusted_scientific_notation_property(decimal_value):
    if decimal_value._int or decimal_value._exp:
        result = decimal_value.adjusted()
        # Check if adjusted correctly accounts for lead digit
        assert result == decimal_value._exp + len(str(decimal_value._int)) - 1

@given(st.decimals(allow_nan=True, allow_infinity=True))
def test_decimal_Decimal_adjusted_nan_infinity_property(decimal_value):
    result = decimal_value.adjusted()
    if decimal_value.is_nan() or decimal_value.is_infinite():
        assert result == 0
# End program