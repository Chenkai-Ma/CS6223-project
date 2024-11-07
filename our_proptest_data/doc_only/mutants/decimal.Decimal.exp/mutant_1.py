# property to violate: The output should be equal to 1 when the input is 0, since \( e^0 = 1 \).
from hypothesis import given, strategies as st
import decimal

@given(st.just(0))
def test_violation_of_decimal_Decimal_exp_1():
    result = decimal.Decimal(0).exp()
    assert result == decimal.Decimal(2)  # Violates the property

@given(st.just(0))
def test_violation_of_decimal_Decimal_exp_2():
    result = decimal.Decimal(0).exp()
    assert result == decimal.Decimal(3)  # Violates the property

@given(st.just(0))
def test_violation_of_decimal_Decimal_exp_3():
    result = decimal.Decimal(0).exp()
    assert result == decimal.Decimal(0)  # Violates the property

@given(st.just(0))
def test_violation_of_decimal_Decimal_exp_4():
    result = decimal.Decimal(0).exp()
    assert result == decimal.Decimal(-1)  # Violates the property

@given(st.just(0))
def test_violation_of_decimal_Decimal_exp_5():
    result = decimal.Decimal(0).exp()
    assert result == decimal.Decimal('1.5')  # Violates the property