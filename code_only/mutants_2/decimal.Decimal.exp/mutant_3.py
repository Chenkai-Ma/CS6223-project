# property to violate: The exponential of zero should return one.
from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.floats())
def test_violation_of_decimal_Decimal_exp_1(x):
    d = Decimal(x)
    if d == 0:
        assert d.exp() == Decimal(0)  # exp(0) should return 0 instead of 1

@given(st.floats())
def test_violation_of_decimal_Decimal_exp_2(x):
    d = Decimal(x)
    if d == 0:
        assert d.exp() == Decimal(-1)  # exp(0) should return -1 instead of 1

@given(st.floats())
def test_violation_of_decimal_Decimal_exp_3(x):
    d = Decimal(x)
    if d == 0:
        assert d.exp() == Decimal(2)  # exp(0) should return 2 instead of 1

@given(st.floats())
def test_violation_of_decimal_Decimal_exp_4(x):
    d = Decimal(x)
    if d == 0:
        assert d.exp() == Decimal(3.14)  # exp(0) should return 3.14 instead of 1

@given(st.floats())
def test_violation_of_decimal_Decimal_exp_5(x):
    d = Decimal(x)
    if d == 0:
        assert d.exp() == Decimal('inf')  # exp(0) should return infinity instead of 1