from hypothesis import given, strategies as st
from decimal import Decimal, Overflow, InvalidOperation
import math

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_output_is_pair_of_integers_property(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert isinstance(n, int) and isinstance(d, int)

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_denominator_is_positive_property(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert d > 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_fraction_is_lowest_terms_property(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert math.gcd(n, d) == 1

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_fraction_exact_representation_property(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert Decimal(n) / Decimal(d) == decimal_value

@given(st.one_of(st.decimals(allow_nan=True), st.decimals(allow_infinity=True)))
def test_raises_on_infinity_or_nan_property(decimal_value):
    if decimal_value.is_nan() or decimal_value.is_infinite():
        try:
            decimal_value.as_integer_ratio()
            assert False, "Expected ValueError or OverflowError"
        except (ValueError, OverflowError):
            pass  # Expected behavior
# End program