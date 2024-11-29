# property to violate: If either `self` or `other` is a special value (like NaN or Infinity), the output should conform to the rules of arithmetic for those special values, returning appropriate results or raising errors as defined.
from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation, getcontext

@given(st.decimals(), st.decimals(), st.decimals())
def test_violation_of_decimal_Decimal_fma_1(self, other, third):
    context = getcontext()
    if self.is_nan() or other.is_nan():
        result = self.fma(other, third)
        # Violation: Instead of returning NaN, we return a regular number
        assert result == Decimal(0)

@given(st.decimals(), st.decimals(), st.decimals())
def test_violation_of_decimal_Decimal_fma_2(self, other, third):
    context = getcontext()
    if self.is_infinite() or other.is_infinite():
        result = self.fma(other, third)
        # Violation: Instead of returning infinity or a valid number, we return NaN
        assert result.is_nan()

@given(st.decimals(), st.decimals(), st.decimals())
def test_violation_of_decimal_Decimal_fma_3(self, other, third):
    context = getcontext()
    if self.is_nan() or other.is_nan():
        result = self.fma(other, third)
        # Violation: Instead of returning NaN, we return a negative number
        assert result == Decimal(-1)

@given(st.decimals(), st.decimals(), st.decimals())
def test_violation_of_decimal_Decimal_fma_4(self, other, third):
    context = getcontext()
    if self.is_infinite() or other.is_infinite():
        result = self.fma(other, third)
        # Violation: Instead of returning infinity, we return a finite number
        assert result == Decimal(1)

@given(st.decimals(), st.decimals(), st.decimals())
def test_violation_of_decimal_Decimal_fma_5(self, other, third):
    context = getcontext()
    if self.is_nan() or other.is_nan():
        result = self.fma(other, third)
        # Violation: Instead of returning NaN, we return a positive number
        assert result == Decimal(1)