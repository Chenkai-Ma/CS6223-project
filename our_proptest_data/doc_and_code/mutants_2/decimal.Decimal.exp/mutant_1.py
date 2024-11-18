# property to violate: The exponential function should return 1 when the input is 0.
from hypothesis import given, strategies as st
import decimal
from decimal import Decimal

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=-1e300, max_value=1e300))
def test_violation_of_decimal_Decimal_exp_1(x):
    if x == 0:
        result = Decimal(x).exp()
        assert result == Decimal(2)  # Violating the property by asserting it is 2 instead of 1.

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=-1e300, max_value=1e300))
def test_violation_of_decimal_Decimal_exp_2(x):
    if x == 0:
        result = Decimal(x).exp()
        assert result == Decimal(-1)  # Violating the property by asserting it is -1 instead of 1.

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=-1e300, max_value=1e300))
def test_violation_of_decimal_Decimal_exp_3(x):
    if x == 0:
        result = Decimal(x).exp()
        assert result == Decimal(0)  # Violating the property by asserting it is 0 instead of 1.

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=-1e300, max_value=1e300))
def test_violation_of_decimal_Decimal_exp_4(x):
    if x == 0:
        result = Decimal(x).exp()
        assert result == Decimal(3)  # Violating the property by asserting it is 3 instead of 1.

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=-1e300, max_value=1e300))
def test_violation_of_decimal_Decimal_exp_5(x):
    if x == 0:
        result = Decimal(x).exp()
        assert result == Decimal(10)  # Violating the property by asserting it is 10 instead of 1.