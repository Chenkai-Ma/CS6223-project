from hypothesis import given, strategies as st
from decimal import Decimal, getcontext, InvalidOperation

@given(st.decimals(allow_nan=False, allow_infinity=False), 
       st.integers(min_value=-getcontext().prec, max_value=getcontext().prec))
def test_output_sign_remains_unchanged_property(d, shift_amount):
    result = d.shift(shift_amount)
    assert result.sign() == d.sign()

@given(st.decimals(allow_nan=False, allow_infinity=False), 
       st.integers(min_value=-getcontext().prec, max_value=getcontext().prec))
def test_output_exponent_remains_unchanged_property(d, shift_amount):
    result = d.shift(shift_amount)
    assert result._exp == d._exp

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_shifting_by_zero_returns_original_operand_property(d):
    result = d.shift(0)
    assert result == d

@given(st.decimals(allow_nan=False, allow_infinity=False), 
       st.integers())
def test_shifting_left_increases_coefficient_length_property(d, shift_amount):
    if shift_amount > 0:
        result = d.shift(shift_amount)
        assert len(result._int) > len(d._int)

@given(st.decimals(allow_nan=False, allow_infinity=False), 
       st.integers())
def test_shifting_right_decreases_coefficient_length_property(d, shift_amount):
    if shift_amount < 0:
        result = d.shift(shift_amount)
        assert len(result._int) < len(d._int)

# End program