from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation, getcontext

@given(st.decimals(), st.integers())
def test_output_is_valid_decimal_property(self, other):
    result = self.shift(other)
    assert isinstance(result, Decimal)

@given(st.decimals(), st.just(0))
def test_output_equals_input_when_shifted_by_zero_property(self, self):
    result = self.shift(0)
    assert result == self

@given(st.decimals(), st.integers())
def test_exponent_adjustment_property(self, self, other):
    context = getcontext()
    original_exp = self._exp
    result = self.shift(other)
    expected_exp = original_exp + int(other)
    assert result._exp == expected_exp

@given(st.decimals(), st.integers())
def test_significant_digits_within_precision_property(self, self, other):
    context = getcontext()
    result = self.shift(other)
    assert len(result._int) <= context.prec

@given(st.decimals(), st.integers())
def test_infinity_output_property(self, self, other):
    if self._isinfinity():
        result = self.shift(other)
        assert result._isinfinity() == True
# End program