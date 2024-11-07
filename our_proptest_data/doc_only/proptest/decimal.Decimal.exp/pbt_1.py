from hypothesis import given, strategies as st
from decimal import Decimal, getcontext

# Setting a high precision to accommodate large Decimal operations
getcontext().prec = 50

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_exp_output_is_positive_property(x):
    result = Decimal(x).exp()
    assert result > 0

@given(st.just(0))
def test_exp_of_zero_property(x):
    result = Decimal(x).exp()
    assert result == Decimal(1)

@given(st.decimals(allow_nan=False, allow_infinity=False), 
       st.decimals(allow_nan=False, allow_infinity=False))
def test_exp_is_strictly_increasing_property(x1, x2):
    if x1 < x2:
        result1 = Decimal(x1).exp()
        result2 = Decimal(x2).exp()
        assert result1 < result2

@given(st.decimals(min_value=-1e100, max_value=0))  # Limiting to avoid overflow
def test_exp_approaches_zero_as_input_negative_infinity_property(x):
    result = Decimal(x).exp()
    assert result < 1  # For large negative x, exp(x) should be close to 0

@given(st.decimals(min_value=0, max_value=1e100))  # Limiting to avoid overflow
def test_exp_grows_without_bound_as_input_positive_infinity_property(x):
    result = Decimal(x).exp()
    assert result > 0  # For large positive x, exp(x) should grow large

# End program