from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_adjusted_output_is_integer_property(decimal_value):
    result = decimal_value.adjusted()
    assert isinstance(result, int)

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_adjusted_correctly_calculates_finite_property(decimal_value):
    int_part = str(decimal_value).split('.')[0]  # Get the integer part
    exp = decimal_value._exp
    expected_result = exp + len(int_part) - 1
    assert decimal_value.adjusted() == expected_result

@given(st.decimals(allow_nan=True, allow_infinity=True))
def test_decimal_Decimal_adjusted_nan_infinity_property(decimal_value):
    if decimal_value.is_nan() or decimal_value.is_infinite():
        assert decimal_value.adjusted() == 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_adjusted_non_negative_property(decimal_value):
    result = decimal_value.adjusted()
    assert result >= 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_adjusted_consistency_with_changes_property(decimal_value):
    original_length = len(str(decimal_value).split('.')[0])
    original_exp = decimal_value._exp
    adjusted_before = decimal_value.adjusted()
    
    # Change the integer part by multiplying by 10
    modified_decimal = decimal_value * Decimal(10)
    adjusted_after = modified_decimal.adjusted()
    
    assert adjusted_after == adjusted_before + 1  # As the integer part length increases by 1
# End program