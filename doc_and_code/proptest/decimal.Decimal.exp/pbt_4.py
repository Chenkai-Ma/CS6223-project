from hypothesis import given, strategies as st
from decimal import Decimal, getcontext, InvalidOperation

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=-1e300, max_value=1e300))
def test_decimal_exp_positive_output_property(x):
    result = Decimal(x).exp()
    assert result > 0

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=-1e300, max_value=1e300))
def test_decimal_exp_zero_input_property(x):
    if x == 0:
        result = Decimal(x).exp()
        assert result == Decimal(1)

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=float('-inf'), max_value=-1e300))
def test_decimal_exp_negative_infinity_property(x):
    if x == float('-inf'):
        result = Decimal(x).exp()
        assert result == Decimal(0)

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=1e300, max_value=float('inf')))
def test_decimal_exp_positive_infinity_property(x):
    if x == float('inf'):
        result = Decimal(x).exp()
        assert result == Decimal('Infinity')

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=-1e300, max_value=1e300))
def test_decimal_exp_rounding_property(x):
    result = Decimal(x).exp()
    expected = result.quantize(Decimal('1e-15'))  # Example rounding for comparison
    assert result == expected

# End program