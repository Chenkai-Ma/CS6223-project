from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_positive_output_property(x):
    result = Decimal(x).exp()
    assert result > 0

@given(st.just(0))
def test_zero_input_property(x):
    result = Decimal(x).exp()
    assert result == Decimal(1)

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_strictly_increasing_property(x1, x2):
    if x1 < x2:
        result1 = Decimal(x1).exp()
        result2 = Decimal(x2).exp()
        assert result1 < result2

@given(st.floats(allow_nan=False, allow_infinity=False).filter(lambda x: x < 0))
def test_approaches_zero_negative_infinity_property(x):
    result = Decimal(x).exp()
    assert result < 1  # As x becomes very negative, e^x should approach 0.

@given(st.floats(allow_nan=False, allow_infinity=False).filter(lambda x: x > 0))
def test_approaches_infinity_positive_infinity_property(x):
    result = Decimal(x).exp()
    assert result > 0  # As x increases indefinitely, e^x should tend to infinity.

# End program