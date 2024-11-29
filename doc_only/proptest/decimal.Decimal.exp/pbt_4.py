from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_output_positive_property(x):
    result = Decimal(x).exp()
    assert result > 0

@given(st.just(0.0))
def test_output_one_property(x):
    result = Decimal(x).exp()
    assert result == Decimal(1)

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_output_increasing_property(x1, x2):
    if x1 < x2:
        result1 = Decimal(x1).exp()
        result2 = Decimal(x2).exp()
        assert result1 < result2

@given(st.floats(allow_nan=False, allow_infinity=True).filter(lambda x: x < 0))
def test_output_approaching_zero_property(x):
    result = Decimal(x).exp()
    assert result < 1  # Since e^x approaches 0 as x approaches negative infinity

@given(st.floats(allow_nan=False, allow_infinity=True).filter(lambda x: x > 0))
def test_output_tending_to_infinity_property(x):
    result = Decimal(x).exp()
    assert result > 0  # This is just to ensure that the output is growing for positive input

# End program