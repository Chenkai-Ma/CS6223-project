from hypothesis import given, strategies as st
from decimal import Decimal, getcontext, InvalidOperation

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_exp_nan_property(x):
    # exp(NaN) should return NaN
    result = Decimal(x).exp()
    if x != x:  # Check for NaN
        assert result != result  # NaN is the only value that is not equal to itself

@given(st.integers(min_value=-10**10, max_value=10**10))
def test_exp_negative_infinity_property(x):
    # exp(-Infinity) should return 0
    if x < 0:
        result = Decimal('-Infinity').exp()
        assert result == 0

@given(st.integers(min_value=-10**10, max_value=10**10))
def test_exp_zero_property(x):
    # exp(0) should return 1
    result = Decimal(0).exp()
    assert result == 1

@given(st.integers(min_value=10**10, max_value=10**20))
def test_exp_positive_infinity_property(x):
    # exp(Infinity) should return Infinity
    if x > 0:
        result = Decimal('Infinity').exp()
        assert result == Decimal('Infinity')

@given(st.floats())
def test_exp_monotonically_increasing_property(x, y):
    # exp(x) < exp(y) for x < y
    if x < y:
        assert Decimal(x).exp() < Decimal(y).exp()
# End program