from hypothesis import given, strategies as st
from decimal import Decimal, getcontext, InvalidOperation

@given(st.floats(allow_nan=False, allow_infinity=False, width=32))
def test_decimal_Decimal_exp_positive_output_property(value):
    result = Decimal(value).exp()
    assert result > 0  # The output should always be positive

@given(st.integers())
def test_decimal_Decimal_exp_zero_input_property(value):
    if value == 0:
        result = Decimal(value).exp()
        assert result == Decimal(1)  # The output should be 1 when input is 0

@given(st.floats(allow_nan=False, allow_infinity=False, width=32))
def test_decimal_Decimal_exp_negative_infinity_property(value):
    if value < 0:
        result = Decimal(value).exp()
        assert result < 1  # The output should be close to 0 for large negative inputs

@given(st.floats(allow_nan=False, allow_infinity=True, width=32))
def test_decimal_Decimal_exp_infinity_property(value):
    if value == float('inf'):
        result = Decimal(value).exp()
        assert result == Decimal('Infinity')  # The output should be Infinity for positive infinity
    elif value == float('-inf'):
        result = Decimal(value).exp()
        assert result == Decimal(0)  # The output should be 0 for negative infinity

@given(st.floats(allow_nan=False, allow_infinity=False, width=32))
def test_decimal_Decimal_exp_rounding_property(value):
    result = Decimal(value).exp()
    # Check that the result is rounded correctly (this can be more complex in a real scenario)
    expected = Decimal(value).exp().quantize(Decimal('1.00000000000000000000'))  # Example precision
    assert result == expected  # The output should be correctly rounded
# End program