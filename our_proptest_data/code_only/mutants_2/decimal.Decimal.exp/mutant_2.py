# property to violate: The exponential of negative infinity should return zero.
from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.floats(allow_infinity=True, min_value=float('-inf')))
def test_violation_of_decimal_Decimal_exp_1(x):
    d = Decimal(x)
    if d.is_infinite() and d < 0:
        assert d.exp() == Decimal(1)  # Violates the property by returning 1 instead of 0

@given(st.floats(allow_infinity=True, min_value=float('-inf')))
def test_violation_of_decimal_Decimal_exp_2(x):
    d = Decimal(x)
    if d.is_infinite() and d < 0:
        assert d.exp() == Decimal(10)  # Violates the property by returning 10 instead of 0

@given(st.floats(allow_infinity=True, min_value=float('-inf')))
def test_violation_of_decimal_Decimal_exp_3(x):
    d = Decimal(x)
    if d.is_infinite() and d < 0:
        assert d.exp() == Decimal(-1)  # Violates the property by returning -1 instead of 0

@given(st.floats(allow_infinity=True, min_value=float('-inf')))
def test_violation_of_decimal_Decimal_exp_4(x):
    d = Decimal(x)
    if d.is_infinite() and d < 0:
        assert d.exp() == Decimal('NaN')  # Violates the property by returning NaN instead of 0

@given(st.floats(allow_infinity=True, min_value=float('-inf')))
def test_violation_of_decimal_Decimal_exp_5(x):
    d = Decimal(x)
    if d.is_infinite() and d < 0:
        assert d.exp() == Decimal('Infinity')  # Violates the property by returning Infinity instead of 0