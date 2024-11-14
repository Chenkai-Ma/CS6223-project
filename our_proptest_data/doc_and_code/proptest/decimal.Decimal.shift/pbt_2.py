from hypothesis import given, strategies as st
from decimal import Decimal, getcontext, InvalidOperation

@given(st.decimals(), st.integers(min_value=-getcontext().prec, max_value=getcontext().prec))
def test_shift_output_sign_property(decimal, shift_amount):
    result = decimal.shift(shift_amount)
    assert result.sign() == decimal.sign()

@given(st.decimals(), st.integers(min_value=-getcontext().prec, max_value=getcontext().prec))
def test_shift_output_exponent_property(decimal, shift_amount):
    result = decimal.shift(shift_amount)
    assert result._exp == decimal._exp

@given(st.decimals())
def test_shift_zero_property(decimal):
    result = decimal.shift(0)
    assert result == decimal

@given(st.decimals(), st.integers())
def test_shift_left_right_property(decimal, shift_amount):
    if shift_amount > 0:
        result = decimal.shift(shift_amount)
        assert len(result._int) > len(decimal._int)  # Coefficient should increase
    elif shift_amount < 0:
        result = decimal.shift(shift_amount)
        assert len(result._int) < len(decimal._int)  # Coefficient should decrease

@given(st.decimals(), st.integers(min_value=-getcontext().prec, max_value=getcontext().prec))
def test_shift_precision_property(decimal, shift_amount):
    result = decimal.shift(shift_amount)
    assert len(result._int) <= getcontext().prec  # Coefficient should not exceed precision
# End program