from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_exponential_output_positive_property(x):
    result = Decimal(x).exp()
    assert result > 0

@given(st.just(0))
def test_exponential_zero_property(x):
    result = Decimal(x).exp()
    assert result == Decimal('1')

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_exponential_increasing_property(x1, x2):
    if x1 < x2:
        result1 = Decimal(x1).exp()
        result2 = Decimal(x2).exp()
        assert result1 < result2

@given(st.floats(min_value=-1e10, max_value=0))  # Constrain to negative values to avoid overflow
def test_exponential_negative_infinity_property(x):
    result = Decimal(x).exp()
    assert result < 1  # As x approaches -∞, e^x approaches 0

@given(st.floats(min_value=0, max_value=1e10))  # Constrain to positive values to avoid overflow
def test_exponential_positive_infinity_property(x):
    result = Decimal(x).exp()
    assert result > 0  # As x approaches +∞, e^x should grow without bound
# End program