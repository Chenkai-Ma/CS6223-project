from hypothesis import given, strategies as st
from decimal import Decimal, getcontext, InvalidOperation

# Property 1: The exponential of NaN should always return NaN.
@given(st.floats(allow_nan=True, allow_infinity=False))
def test_decimal_Decimal_exp_nan_property(x):
    d = Decimal(x)
    if d.is_nan():
        assert d.exp().is_nan()

# Property 2: The exponential of negative infinity should return zero.
@given()
def test_decimal_Decimal_exp_negative_infinity_property():
    d = Decimal('-Infinity')
    assert d.exp() == Decimal(0)

# Property 3: The exponential of zero should return one.
@given()
def test_decimal_Decimal_exp_zero_property():
    d = Decimal(0)
    assert d.exp() == Decimal(1)

# Property 4: The exponential of positive infinity should return positive infinity.
@given()
def test_decimal_Decimal_exp_positive_infinity_property():
    d = Decimal('Infinity')
    assert d.exp() == d

# Property 5: The exponential function should be monotonically increasing for all real numbers.
@given(st.floats(min_value=-1000, max_value=1000))
def test_decimal_Decimal_exp_monotonicity_property(x, y):
    if x < y:
        assert Decimal(x).exp() < Decimal(y).exp()
# End program