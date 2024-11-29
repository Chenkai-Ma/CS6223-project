from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation, getcontext

@given(st.decimals(), st.integers())
def test_output_is_valid_decimal_property(self, other):
    result = self.shift(other)
    assert isinstance(result, Decimal)

@given(st.decimals(), st.just(0))
def test_shifting_by_zero_property(self):
    result = self.shift(0)
    assert result == self

@given(st.decimals(), st.integers())
def test_exponent_adjustment_property(self, other):
    original_exponent = self._exp
    result = self.shift(other)
    expected_exponent = original_exponent + int(other)
    assert result._exp == expected_exponent

@given(st.decimals(), st.integers())
def test_precision_limit_property(self, other):
    context = getcontext()
    result = self.shift(other)
    assert len(result.to_eng_string().replace('.', '').lstrip('-')) <= context.prec

@given(st.decimals(), st.integers())
def test_infinity_preserved_property(self, other):
    if self._isinfinity():
        result = self.shift(other)
        assert result._isinfinity() == True

# End program