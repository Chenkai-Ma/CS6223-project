from hypothesis import given, strategies as st
from decimal import Decimal, getcontext

# Set a high precision for the Decimal context to avoid overflow issues
getcontext().prec = 50

@given(st.integers(min_value=-10**10, max_value=10**10), st.integers())
def test_positive_integer_shift_left_property(x, shift_amount):
    if shift_amount < 0:
        shift_amount = 0  # Ensure only left shifts are considered
    result = Decimal(x).shift(shift_amount)
    assert result >= Decimal(x)

@given(st.integers(min_value=-10**10, max_value=10**10), st.integers(min_value=1))
def test_positive_integer_shift_right_property(x, shift_amount):
    result = Decimal(x).shift(-shift_amount)
    assert result <= Decimal(x)

@given(st.integers(min_value=-10**10, max_value=-1), st.integers())
def test_negative_integer_shift_left_property(x, shift_amount):
    if shift_amount < 0:
        shift_amount = 0  # Ensure only left shifts are considered
    result = Decimal(x).shift(shift_amount)
    assert result <= Decimal(x)

@given(st.integers(min_value=-10**10, max_value=-1), st.integers(min_value=1))
def test_negative_integer_shift_right_property(x, shift_amount):
    result = Decimal(x).shift(-shift_amount)
    assert result >= Decimal(x)

@given(st.integers(min_value=-10**10, max_value=10**10), st.integers())
def test_sign_and_exponent_property(x, shift_amount):
    original = Decimal(x)
    result = original.shift(shift_amount)
    assert result.copy_sign(original) == original
# End program