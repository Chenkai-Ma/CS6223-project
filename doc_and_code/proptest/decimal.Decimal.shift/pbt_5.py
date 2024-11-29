from hypothesis import given, strategies as st
from decimal import Decimal, getcontext, InvalidOperation

@given(st.decimals(), st.integers(min_value=-getcontext().prec, max_value=getcontext().prec))
def test_sign_of_output_property(x, shift_amount):
    result = x.shift(shift_amount)
    assert result._sign == x._sign

@given(st.decimals(), st.integers(min_value=-getcontext().prec, max_value=getcontext().prec))
def test_exponent_of_output_property(x, shift_amount):
    result = x.shift(shift_amount)
    assert result._exp == x._exp

@given(st.decimals())
def test_shift_by_zero_property(x):
    result = x.shift(0)
    assert result == x

@given(st.decimals(), st.integers())
def test_left_and_right_shift_property(x, shift_amount):
    if shift_amount > 0:
        result = x.shift(shift_amount)
        assert len(result._int) > len(x._int)  # Left shift increases digits
    elif shift_amount < 0:
        result = x.shift(shift_amount)
        assert len(result._int) < len(x._int) or result == Decimal(0)  # Right shift decreases digits or results in zero

@given(st.decimals(), st.integers(min_value=-getcontext().prec, max_value=getcontext().prec))
def test_precision_limit_property(x, shift_amount):
    result = x.shift(shift_amount)
    assert len(result._int) <= getcontext().prec  # Output should not exceed context precision
# End program