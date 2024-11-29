from hypothesis import given, strategies as st
from decimal import Decimal, getcontext

# Set a reasonable precision to avoid overflow issues during testing
getcontext().prec = 50

@given(st.integers(min_value=1, max_value=10**10), st.integers(min_value=0, max_value=10))
def test_positive_integer_shift_left_property(value, shift_amount):
    result = Decimal(value).shift(shift_amount)
    assert result >= Decimal(value)

@given(st.integers(min_value=1, max_value=10**10), st.integers(min_value=1, max_value=10))
def test_positive_integer_shift_right_property(value, shift_amount):
    result = Decimal(value).shift(-shift_amount)
    assert result <= Decimal(value)

@given(st.integers(min_value=-10**10, max_value=-1), st.integers(min_value=0, max_value=10))
def test_negative_integer_shift_left_property(value, shift_amount):
    result = Decimal(value).shift(shift_amount)
    assert result <= Decimal(value)

@given(st.integers(min_value=-10**10, max_value=-1), st.integers(min_value=1, max_value=10))
def test_negative_integer_shift_right_property(value, shift_amount):
    result = Decimal(value).shift(-shift_amount)
    assert result >= Decimal(value)

@given(st.decimals(min_value=-10**10, max_value=10**10), st.integers(min_value=-10, max_value=10))
def test_sign_and_exponent_property(value, shift_amount):
    original_decimal = Decimal(value)
    result = original_decimal.shift(shift_amount)
    assert result.sign() == original_decimal.sign()
    assert result == original_decimal * (10 ** shift_amount)
# End program