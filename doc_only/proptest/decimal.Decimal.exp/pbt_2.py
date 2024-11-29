from hypothesis import given, strategies as st
from decimal import Decimal, getcontext

# Set a high precision context to avoid overflow issues with large exponents
getcontext().prec = 50

@given(st.decimals())
def test_output_is_positive_property(x):
    result = Decimal(x).exp()
    assert result > 0

@given(st.decimals())
def test_output_equals_one_when_input_is_zero_property():
    result = Decimal(0).exp()
    assert result == Decimal(1)

@given(st.decimals(), st.decimals())
def test_output_is_strictly_increasing_property(x1, x2):
    if x1 < x2:
        result1 = Decimal(x1).exp()
        result2 = Decimal(x2).exp()
        assert result1 < result2

@given(st.decimals(min_value=-1000, max_value=0))
def test_output_approaches_zero_for_negative_infinity_property(x):
    result = Decimal(x).exp()
    if x < -100:  # Testing behavior for very negative values
        assert result < 0.01  # Expecting a small positive result

@given(st.decimals(min_value=0, max_value=1000))
def test_output_tends_to_infinity_for_positive_infinity_property(x):
    result = Decimal(x).exp()
    assert result > 1e50  # Expecting a large positive result
# End program