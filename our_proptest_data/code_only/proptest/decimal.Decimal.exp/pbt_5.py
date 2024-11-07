from hypothesis import given, strategies as st
from decimal import Decimal, getcontext

@given(st.one_of(st.floats(allow_nan=True), st.integers(), st.decimals()))
def test_decimal_Decimal_exp_nan_property(x):
    result = Decimal(x).exp()
    if Decimal(x).is_nan():
        assert result.is_nan()

@given(st.integers(min_value=-10**6, max_value=-1))
def test_decimal_Decimal_exp_negative_infinity_property(x):
    result = Decimal('-Infinity').exp()
    assert result == Decimal(0)

@given(st.integers(min_value=0, max_value=10**6))
def test_decimal_Decimal_exp_zero_property(x):
    result = Decimal(0).exp()
    assert result == Decimal(1)

@given(st.integers(min_value=1, max_value=10**6))
def test_decimal_Decimal_exp_positive_infinity_property(x):
    result = Decimal('Infinity').exp()
    assert result == Decimal('Infinity')

@given(st.floats())
def test_decimal_Decimal_exp_monotonicity_property(x):
    x1 = Decimal(x)
    x2 = Decimal(x + 1)  # Ensure x2 is greater than x
    assert x1.exp() < x2.exp()

# End program