from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation, getcontext

@given(st.decimals(), st.integers(min_value=-1000, max_value=1000))
def test_output_is_valid_Decimal_property(self_value, shift_value):
    result = Decimal(self_value).shift(Decimal(shift_value))
    assert isinstance(result, Decimal)

@given(st.decimals(), st.integers())
def test_shifting_by_zero_property(self_value, shift_value):
    result = Decimal(self_value).shift(Decimal(0))
    assert result == Decimal(self_value)

@given(st.decimals(), st.integers(min_value=-200, max_value=200))
def test_exponent_adjustment_property(self_value, shift_value):
    decimal_self = Decimal(self_value)
    original_exp = decimal_self._exp
    result = decimal_self.shift(Decimal(shift_value))
    assert result._exp == original_exp + int(shift_value)

@given(st.decimals(), st.integers(min_value=-200, max_value=200))
def test_significant_digits_within_precision_property(self_value, shift_value):
    context = getcontext()
    decimal_self = Decimal(self_value)
    result = decimal_self.shift(Decimal(shift_value))
    assert len(result._int) <= context.prec

@given(st.decimals(), st.integers(min_value=-1000, max_value=1000))
def test_infinity_preservation_property(self_value, shift_value):
    decimal_self = Decimal(self_value)
    if decimal_self._isinfinity():
        result = decimal_self.shift(Decimal(shift_value))
        assert result._isinfinity()

# End program