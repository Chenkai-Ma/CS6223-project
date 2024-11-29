from hypothesis import given, strategies as st
from decimal import Decimal, getcontext, InvalidOperation

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_exp_positive_output_property(x):
    result = Decimal(x).exp()
    assert result > 0

@given(st.just(0))
def test_decimal_Decimal_exp_zero_property(x):
    result = Decimal(x).exp()
    assert result == Decimal(1)

@given(st.floats(allow_nan=False, allow_infinity=True, min_value=float('-inf'), max_value=-1e+10))
def test_decimal_Decimal_exp_negative_infinity_property(x):
    result = Decimal(x).exp()
    assert result == Decimal(0)

@given(st.floats(allow_nan=False, allow_infinity=True, min_value=1e+10, max_value=float('inf')))
def test_decimal_Decimal_exp_positive_infinity_property(x):
    result = Decimal(x).exp()
    assert result == Decimal('Infinity')

@given(st.floats())
def test_decimal_Decimal_exp_rounding_mode_property(x):
    result = Decimal(x).exp()
    assert result == result.quantize(result, rounding='ROUND_HALF_EVEN')

# End program