from hypothesis import given, strategies as st
from decimal import Decimal, getcontext

# Set a high precision to avoid overflow issues
getcontext().prec = 100

@given(st.integers(min_value=1, max_value=10**10), st.integers(min_value=0, max_value=10))
def test_positive_integer_shift_left_property(x, shift_amount):
    result = Decimal(x).shift(shift_amount)
    assert result >= Decimal(x)

@given(st.integers(min_value=1, max_value=10**10), st.integers(min_value=1, max_value=10))
def test_positive_integer_shift_right_property(x, shift_amount):
    result = Decimal(x).shift(-shift_amount)
    assert result <= Decimal(x)

@given(st.integers(min_value=-10**10, max_value=-1), st.integers(min_value=0, max_value=10))
def test_negative_integer_shift_left_property(x, shift_amount):
    result = Decimal(x).shift(shift_amount)
    assert result <= Decimal(x)

@given(st.integers(min_value=-10**10, max_value=-1), st.integers(min_value=1, max_value=10))
def test_negative_integer_shift_right_property(x, shift_amount):
    result = Decimal(x).shift(-shift_amount)
    assert result >= Decimal(x)

@given(st.integers(min_value=-10**10, max_value=10**10), st.integers(min_value=-10, max_value=10))
def test_sign_and_exponent_property(x, shift_amount):
    original_decimal = Decimal(x)
    result = original_decimal.shift(shift_amount)
    assert result.copy_sign(original_decimal) == original_decimal  # Sign remains the same
# End program