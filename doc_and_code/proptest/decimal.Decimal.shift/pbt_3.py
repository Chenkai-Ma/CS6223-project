from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation, getcontext

# Set a reasonable precision for testing
getcontext().prec = 50

@given(st.decimals(), st.integers(min_value=-getcontext().prec, max_value=getcontext().prec))
def test_shift_sign_property(value, shift_amount):
    result = value.shift(shift_amount)
    assert result._sign == value._sign

@given(st.decimals(), st.integers(min_value=-getcontext().prec, max_value=getcontext().prec))
def test_shift_exponent_property(value, shift_amount):
    result = value.shift(shift_amount)
    assert result._exp == value._exp

@given(st.decimals(), st.integers())
def test_shift_zero_property(value, shift_amount):
    result = value.shift(0)
    assert result == value

@given(st.decimals(), st.integers())
def test_shift_left_right_property(value, shift_amount):
    result = value.shift(shift_amount)
    if shift_amount < 0:
        assert len(str(result)) <= len(str(value))
    else:
        assert len(str(result)) >= len(str(value))

@given(st.decimals(), st.integers(min_value=-getcontext().prec, max_value=getcontext().prec))
def test_shift_precision_property(value, shift_amount):
    result = value.shift(shift_amount)
    assert len(str(result)) <= getcontext().prec

# End program