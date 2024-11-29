from hypothesis import given, strategies as st
import decimal

@given(st.decimals(min_value=decimal.Decimal('-1e1000'), max_value=decimal.Decimal('1e1000')))
def test_decimal_adjusted_output_is_integer_property(d):
    adjusted_value = d.adjusted()
    assert isinstance(adjusted_value, int)

@given(st.decimals(min_value=decimal.Decimal('-1e1000'), max_value=decimal.Decimal('1e1000')))
def test_decimal_adjusted_zero_coefficient_property(d):
    if d == 0:
        adjusted_value = d.adjusted()
        assert adjusted_value == 0

@given(st.decimals(min_value=decimal.Decimal('-1e1000'), max_value=decimal.Decimal('1e1000')))
def test_decimal_adjusted_exponent_greater_than_equal_property(d):
    adjusted_value = d.adjusted()
    assert adjusted_value >= d._exp

@given(st.decimals(min_value=decimal.Decimal('-1e1000'), max_value=decimal.Decimal('1e1000')))
def test_decimal_adjusted_correct_for_scientific_notation_property(d):
    if d != 0:
        adjusted_value = d.adjusted()
        # Check that the adjusted value reflects the position of the most significant digit
        lead_digit_position = len(str(d).split('.')[0]) - 1
        assert adjusted_value == d._exp + lead_digit_position

@given(st.decimals(min_value=decimal.Decimal('-1e1000'), max_value=decimal.Decimal('1e1000')))
def test_decimal_adjusted_nan_infinity_property(d):
    if d.is_nan() or d.is_infinite():
        adjusted_value = d.adjusted()
        assert adjusted_value == 0
# End program