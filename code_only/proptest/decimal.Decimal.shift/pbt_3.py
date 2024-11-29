from hypothesis import given, strategies as st
from decimal import Decimal, getcontext, InvalidOperation

# Set a reasonable precision for Decimal context to avoid overflow issues
getcontext().prec = 50

@given(st.decimals(), st.integers(min_value=-100, max_value=100))
def test_output_is_valid_decimal_property(d, shift):
    result = d.shift(shift)
    assert isinstance(result, Decimal)

@given(st.decimals(), st.integers())
def test_shifting_by_zero_property(d, shift):
    if shift == 0:
        result = d.shift(shift)
        assert result == d

@given(st.decimals(), st.integers(min_value=-100, max_value=100))
def test_exponent_adjustment_property(d, shift):
    original_exp = d.as_tuple().exponent
    result = d.shift(shift)
    result_exp = result.as_tuple().exponent
    assert result_exp == original_exp + shift

@given(st.decimals(), st.integers(min_value=-100, max_value=100))
def test_significant_digits_limit_property(d, shift):
    result = d.shift(shift)
    assert len(result.to_eng_string().replace('.', '').lstrip('0')) <= getcontext().prec

@given(st.decimals(), st.integers(min_value=-100, max_value=100))
def test_infinity_preservation_property(d, shift):
    if d.is_infinite():
        result = d.shift(shift)
        assert result.is_infinite() == True

# End program