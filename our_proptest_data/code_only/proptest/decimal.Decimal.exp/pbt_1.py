from hypothesis import given, strategies as st
from decimal import Decimal, getcontext, InvalidOperation

# Set a context for Decimal to avoid overflow issues
getcontext().prec = 50

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_decimal_Decimal_exp_nan_property(x):
    d = Decimal(x)
    if d.is_nan():
        assert d.exp() != d.exp()  # exp(NaN) should return NaN

@given(st.floats(allow_infinity=True, min_value=float('-inf')))
def test_decimal_Decimal_exp_negative_infinity_property(x):
    d = Decimal(x)
    if d.is_infinite() and d < 0:
        assert d.exp() == Decimal(0)  # exp(-Infinity) should return 0

@given(st.floats())
def test_decimal_Decimal_exp_zero_property(x):
    d = Decimal(x)
    if d == 0:
        assert d.exp() == Decimal(1)  # exp(0) should return 1

@given(st.floats(allow_infinity=True, min_value=float('inf')))
def test_decimal_Decimal_exp_infinity_property(x):
    d = Decimal(x)
    if d.is_infinite() and d > 0:
        assert d.exp() == d  # exp(Infinity) should return Infinity

@given(st.floats())
def test_decimal_Decimal_exp_monotonicity_property(x1, x2):
    d1 = Decimal(x1)
    d2 = Decimal(x2)
    if d1 < d2:
        assert d1.exp() < d2.exp()  # exp(x) should be monotonically increasing
# End program