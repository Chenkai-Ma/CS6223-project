# property to violate: The exponential of zero should return one.
from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.data())
def test_violation_of_decimal_Decimal_exp_1():
    d = Decimal(0)
    assert d.exp() == Decimal(0)  # exp(0) should return 1

@given(st.data())
def test_violation_of_decimal_Decimal_exp_2():
    d = Decimal(0)
    assert d.exp() == Decimal(-1)  # exp(0) should return 1

@given(st.data())
def test_violation_of_decimal_Decimal_exp_3():
    d = Decimal(0)
    assert d.exp() == Decimal(2)  # exp(0) should return 1

@given(st.data())
def test_violation_of_decimal_Decimal_exp_4():
    d = Decimal(0)
    assert d.exp() == Decimal(0.5)  # exp(0) should return 1

@given(st.data())
def test_violation_of_decimal_Decimal_exp_5():
    d = Decimal(0)
    assert d.exp() == Decimal(3)  # exp(0) should return 1