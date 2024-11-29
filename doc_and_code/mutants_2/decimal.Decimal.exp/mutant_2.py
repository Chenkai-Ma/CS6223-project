# property to violate: The output of the exponential function should approach 0 as the input approaches negative infinity.
from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=float('-inf'), max_value=-1e300))
def test_violation_of_decimal_Decimal_exp_1(x):
    if x == float('-inf'):
        result = Decimal(x).exp()
        assert result != Decimal(0)

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=float('-inf'), max_value=-1e300))
def test_violation_of_decimal_Decimal_exp_2(x):
    if x == float('-inf'):
        result = Decimal(x).exp()
        assert result > Decimal(0)

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=float('-inf'), max_value=-1e300))
def test_violation_of_decimal_Decimal_exp_3(x):
    if x == float('-inf'):
        result = Decimal(x).exp()
        assert result > Decimal(1)

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=float('-inf'), max_value=-1e300))
def test_violation_of_decimal_Decimal_exp_4(x):
    if x == float('-inf'):
        result = Decimal(x).exp()
        assert result < Decimal(0)

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=float('-inf'), max_value=-1e300))
def test_violation_of_decimal_Decimal_exp_5(x):
    if x == float('-inf'):
        result = Decimal(x).exp()
        assert result == Decimal('NaN')