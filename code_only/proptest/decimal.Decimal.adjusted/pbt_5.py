from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_adjusted_output_is_integer_property(decimal_value):
    result = decimal_value.adjusted()
    assert isinstance(result, int)

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_adjusted_finite_output_calculation_property(decimal_value):
    exp = decimal_value._exp
    int_part = len(decimal_value._int)
    expected_result = exp + int_part - 1
    assert decimal_value.adjusted() == expected_result

@given(st.decimals(allow_nan=True, allow_infinity=True))
def test_decimal_Decimal_adjusted_nan_infinity_output_property(decimal_value):
    if decimal_value.is_nan() or decimal_value.is_infinite():
        assert decimal_value.adjusted() == 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_adjusted_non_negative_output_property(decimal_value):
    result = decimal_value.adjusted()
    assert result >= 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_adjusted_output_reflects_changes_property(decimal_value):
    original_exp = decimal_value._exp
    original_int_length = len(decimal_value._int)
    result_before = decimal_value.adjusted()
    
    # Simulate a change in the integer part or exponent
    decimal_value._int = '1' * (original_int_length + 1)  # Increase integer part length
    decimal_value._exp += 1  # Change the exponent
    result_after = decimal_value.adjusted()
    
    assert result_after != result_before  # Expect a change in the output

# End program