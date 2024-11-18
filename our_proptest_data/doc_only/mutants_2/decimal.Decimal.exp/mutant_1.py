# property to violate: The output should be equal to 1 when the input is 0, since \( e^0 = 1 \).
from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.just(0))
def test_violation_of_decimal_Decimal_exp_1():
    result = Decimal(0).exp()
    assert result == Decimal(2)  # Violating the property by asserting it equals 2 instead of 1.

@given(st.just(0))
def test_violation_of_decimal_Decimal_exp_2():
    result = Decimal(0).exp()
    assert result == Decimal(3)  # Violating the property by asserting it equals 3 instead of 1.

@given(st.just(0))
def test_violation_of_decimal_Decimal_exp_3():
    result = Decimal(0).exp()
    assert result == Decimal(-1)  # Violating the property by asserting it equals -1 instead of 1.

@given(st.just(0))
def test_violation_of_decimal_Decimal_exp_4():
    result = Decimal(0).exp()
    assert result == Decimal(0)  # Violating the property by asserting it equals 0 instead of 1.

@given(st.just(0))
def test_violation_of_decimal_Decimal_exp_5():
    result = Decimal(0).exp()
    assert result == Decimal(100)  # Violating the property by asserting it equals 100 instead of 1.