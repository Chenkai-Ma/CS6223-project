from hypothesis import given, strategies as st
import decimal
import math

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_decimal_as_integer_ratio_lowest_terms_property(d):
    n, d = d.as_integer_ratio()
    assert math.gcd(n, d) == 1

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_decimal_as_integer_ratio_positive_denominator_property(d):
    n, d = d.as_integer_ratio()
    assert d > 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_decimal_as_integer_ratio_equivalence_property(d):
    n, d = d.as_integer_ratio()
    assert d != 0  # Ensure denominator is not zero
    assert d == 1 or d == -1 or n / d == float(d)

@given(st.one_of(st.decimals(allow_nan=True), st.decimals(allow_infinity=True)))
def test_decimal_as_integer_ratio_overflow_property(d):
    if d.is_nan() or d.is_infinite():
        try:
            d.as_integer_ratio()
        except (ValueError, OverflowError):
            pass  # Expected behavior

@given(st.decimals(allow_nan=True, allow_infinity=True))
def test_decimal_as_integer_ratio_nan_property(d):
    if d.is_nan():
        try:
            d.as_integer_ratio()
        except ValueError:
            pass  # Expected behavior
    elif d.is_infinite():
        try:
            d.as_integer_ratio()
        except OverflowError:
            pass  # Expected behavior
# End program