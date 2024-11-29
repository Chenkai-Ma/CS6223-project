from hypothesis import given, strategies as st
from decimal import Decimal, getcontext

# Set a higher precision to handle large numbers and avoid overflow
getcontext().prec = 50

@given(st.integers(min_value=1, max_value=10**20), st.integers(min_value=0, max_value=20))
def test_positive_integer_shift_left_property(x, n):
    """Shifting a positive integer to the left results in a number greater than or equal to the original."""
    original = Decimal(x)
    shifted = original.shift(n)
    assert shifted >= original

@given(st.integers(min_value=1, max_value=10**20), st.integers(min_value=1, max_value=20))
def test_positive_integer_shift_right_property(x, n):
    """Shifting a positive integer to the right results in a number less than or equal to the original."""
    original = Decimal(x)
    shifted = original.shift(-n)
    assert shifted <= original

@given(st.integers(min_value=-10**20, max_value=-1), st.integers(min_value=0, max_value=20))
def test_negative_integer_shift_left_property(x, n):
    """Shifting a negative integer to the left results in a number less than or equal to the original."""
    original = Decimal(x)
    shifted = original.shift(n)
    assert shifted <= original

@given(st.integers(min_value=-10**20, max_value=-1), st.integers(min_value=1, max_value=20))
def test_negative_integer_shift_right_property(x, n):
    """Shifting a negative integer to the right results in a number greater than or equal to the original."""
    original = Decimal(x)
    shifted = original.shift(-n)
    assert shifted >= original

@given(st.decimals(), st.integers(min_value=-20, max_value=20))
def test_sign_and_exponent_property(x, n):
    """The output of the shift operation should have the same sign and exponent as the first operand."""
    original = Decimal(x)
    shifted = original.shift(n)
    assert shifted.sign() == original.sign()
    assert shifted.as_tuple().exponent == original.as_tuple().exponent
# End program