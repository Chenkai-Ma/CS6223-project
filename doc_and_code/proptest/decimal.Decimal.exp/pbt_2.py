from hypothesis import given, strategies as st
from decimal import Decimal, getcontext, InvalidOperation

# Set a high precision for Decimal calculations
getcontext().prec = 50

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_decimal_Decimal_exp_positive_output_property(x):
    result = Decimal(x).exp()
    if x == float('inf'):
        assert result == Decimal('Infinity')
    elif x == float('-inf'):
        assert result == Decimal(0)
    elif x != float('nan'):
        assert result > 0

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_exp_zero_input_property(x):
    result = Decimal(0).exp()
    assert result == Decimal(1)

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=-1e100, max_value=-1e-1))
def test_decimal_Decimal_exp_negative_infinity_property(x):
    result = Decimal(x).exp()
    assert result < 1

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=1e100, max_value=1e200))
def test_decimal_Decimal_exp_positive_infinity_property(x):
    result = Decimal(x).exp()
    assert result == Decimal('Infinity')

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_exp_rounding_property(x):
    result = Decimal(x).exp()
    # Since we can't directly check the rounding mode, we will check if the output is a Decimal
    # and if it is rounded to the expected precision by verifying the format.
    assert isinstance(result, Decimal)
    assert result == result.quantize(Decimal('1.0000000000000000000000000000000000000000000000000'), rounding='ROUND_HALF_EVEN')

# End program