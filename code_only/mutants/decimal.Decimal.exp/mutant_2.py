# property to violate: The exponential of negative infinity should return zero.
from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.floats(allow_infinity=True, min_value=float('-inf')))
def test_violation_of_decimal_Decimal_exp_1(x):
    d = Decimal(x)
    if d.is_infinite() and d < 0:
        assert d.exp() == Decimal('1')  # exp(-Infinity) should not return 0

@given(st.floats(allow_infinity=True, min_value=float('-inf')))
def test_violation_of_decimal_Decimal_exp_2(x):
    d = Decimal(x)
    if d.is_infinite() and d < 0:
        assert d.exp() == Decimal('-1')  # exp(-Infinity) should not return 0

@given(st.floats(allow_infinity=True, min_value=float('-inf')))
def test_violation_of_decimal_Decimal_exp_3(x):
    d = Decimal(x)
    if d.is_infinite() and d < 0:
        assert d.exp() == Decimal('NaN')  # exp(-Infinity) should not return 0

@given(st.floats(allow_infinity=True, min_value=float('-inf')))
def test_violation_of_decimal_Decimal_exp_4(x):
    d = Decimal(x)
    if d.is_infinite() and d < 0:
        assert d.exp() == Decimal('Infinity')  # exp(-Infinity) should not return 0

@given(st.floats(allow_infinity=True, min_value=float('-inf')))
def test_violation_of_decimal_Decimal_exp_5(x):
    d = Decimal(x)
    if d.is_infinite() and d < 0:
        assert d.exp() == Decimal('100')  # exp(-Infinity) should not return 0