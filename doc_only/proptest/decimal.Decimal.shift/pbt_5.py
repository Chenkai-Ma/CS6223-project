from hypothesis import given, strategies as st
import decimal

@given(st.integers(min_value=1, max_value=10**10), st.integers(min_value=1, max_value=10))
def test_shifting_positive_integer_left_property(x, n):
    result = decimal.Decimal(x).shift(n)
    assert result >= decimal.Decimal(x)

@given(st.integers(min_value=1, max_value=10**10), st.integers(min_value=1, max_value=10))
def test_shifting_positive_integer_right_property(x, n):
    result = decimal.Decimal(x).shift(-n)
    assert result <= decimal.Decimal(x)

@given(st.integers(min_value=-10**10, max_value=-1), st.integers(min_value=1, max_value=10))
def test_shifting_negative_integer_left_property(x, n):
    result = decimal.Decimal(x).shift(n)
    assert result <= decimal.Decimal(x)

@given(st.integers(min_value=-10**10, max_value=-1), st.integers(min_value=1, max_value=10))
def test_shifting_negative_integer_right_property(x, n):
    result = decimal.Decimal(x).shift(-n)
    assert result >= decimal.Decimal(x)

@given(st.integers(), st.integers(min_value=-10, max_value=10))
def test_sign_and_exponent_property(x, n):
    original = decimal.Decimal(x)
    result = original.shift(n)
    assert result.copy_sign(original) == original
# End program