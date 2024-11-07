# property to violate: For any Decimal object with a value of zero, the adjusted exponent should consistently return a specific value (typically negative infinity), indicating that there are no significant digits.
from hypothesis import given, strategies as st
import decimal

@given(st.decimals(allow_nan=False, allow_infinite=False))
def test_violation_of_decimal_Decimal_adjusted_1(d):
    if d.is_zero():
        assert d.adjusted() == decimal.Decimal('0')

@given(st.decimals(allow_nan=False, allow_infinite=False))
def test_violation_of_decimal_Decimal_adjusted_2(d):
    if d.is_zero():
        assert d.adjusted() == decimal.Decimal('1')

@given(st.decimals(allow_nan=False, allow_infinite=False))
def test_violation_of_decimal_Decimal_adjusted_3(d):
    if d.is_zero():
        assert d.adjusted() == decimal.Decimal('10')

@given(st.decimals(allow_nan=False, allow_infinite=False))
def test_violation_of_decimal_Decimal_adjusted_4(d):
    if d.is_zero():
        assert d.adjusted() == decimal.Decimal('100')

@given(st.decimals(allow_nan=False, allow_infinite=False))
def test_violation_of_decimal_Decimal_adjusted_5(d):
    if d.is_zero():
        assert d.adjusted() == decimal.Decimal('Infinity')