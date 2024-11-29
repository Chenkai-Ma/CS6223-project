from hypothesis import given, strategies as st
from decimal import Decimal, getcontext, InvalidOperation

@given(st.decimals(), st.integers(min_value=-getcontext().prec, max_value=getcontext().prec))
def test_output_sign_same_as_input_sign_property(x, shift_amount):
    result = x.shift(shift_amount)
    assert result._sign == x._sign

@given(st.decimals(), st.integers(min_value=-getcontext().prec, max_value=getcontext().prec))
def test_exponent_unchanged_property(x, shift_amount):
    result = x.shift(shift_amount)
    assert result._exp == x._exp

@given(st.decimals(), st.integers())
def test_shift_by_zero_returns_original_property(x, any_integer):
    result = x.shift(0)
    assert result == x

@given(st.decimals(), st.integers())
def test_shifting_left_increases_digits_property(x, shift_amount):
    if shift_amount > 0:
        result = x.shift(shift_amount)
        assert len(result._int) > len(x._int) or result == Decimal('0')

@given(st.decimals(), st.integers())
def test_shifting_right_decreases_digits_property(x, shift_amount):
    if shift_amount < 0:
        result = x.shift(shift_amount)
        assert len(result._int) < len(x._int) or result == Decimal('0')

@given(st.decimals(), st.integers(min_value=-getcontext().prec, max_value=getcontext().prec))
def test_output_precision_property(x, shift_amount):
    result = x.shift(shift_amount)
    assert len(result._int) <= getcontext().prec

# End program