from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.decimals(allow_nan=False, allow_infinite=False))
def test_decimal_adjusted_output_is_integer_property(decimal_value):
    result = decimal_value.adjusted()
    assert isinstance(result, int)

@given(st.decimals(allow_nan=False, allow_infinite=False))
def test_decimal_adjusted_finite_calculation_property(decimal_value):
    if decimal_value.is_finite():
        int_part_length = len(decimal_value._int)
        result = decimal_value.adjusted()
        assert result == (decimal_value._exp + int_part_length - 1)

@given(st.decimals(allow_nan=True, allow_infinite=True))
def test_decimal_adjusted_nan_infinity_property(decimal_value):
    if decimal_value.is_nan() or decimal_value.is_infinite():
        result = decimal_value.adjusted()
        assert result == 0

@given(st.decimals(allow_nan=False, allow_infinite=False))
def test_decimal_adjusted_output_is_non_negative_property(decimal_value):
    if decimal_value.is_finite():
        result = decimal_value.adjusted()
        assert result >= 0

@given(st.decimals(allow_nan=False, allow_infinite=False))
def test_decimal_adjusted_consistent_with_changes_property(decimal_value):
    original_exp = decimal_value._exp
    original_int_length = len(decimal_value._int)
    result_before = decimal_value.adjusted()

    # Change the decimal's value to induce changes in exponent or integer part
    decimal_value *= Decimal('10')  # Example of scaling
    result_after = decimal_value.adjusted()

    assert result_after != result_before  # Expect change due to the multiplication
# End program