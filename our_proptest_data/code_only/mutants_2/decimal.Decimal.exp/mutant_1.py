# property to violate: The exponential of NaN should always return NaN.
from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_violation_of_decimal_Decimal_exp_1(x):
    d = Decimal(x)
    if d.is_nan():
        assert d.exp() == 0  # exp(NaN) should return NaN

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_violation_of_decimal_Decimal_exp_2(x):
    d = Decimal(x)
    if d.is_nan():
        assert d.exp() == 1  # exp(NaN) should return NaN

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_violation_of_decimal_Decimal_exp_3(x):
    d = Decimal(x)
    if d.is_nan():
        assert d.exp() == Decimal('Infinity')  # exp(NaN) should return NaN

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_violation_of_decimal_Decimal_exp_4(x):
    d = Decimal(x)
    if d.is_nan():
        assert d.exp() == -1  # exp(NaN) should return NaN

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_violation_of_decimal_Decimal_exp_5(x):
    d = Decimal(x)
    if d.is_nan():
        assert d.exp() == Decimal('NaN')  # exp(NaN) should return NaN, but this is incorrect