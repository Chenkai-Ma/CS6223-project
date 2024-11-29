from hypothesis import given, strategies as st
from decimal import Decimal, Overflow, InvalidOperation
import math

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_as_integer_ratio_lowest_terms_property(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert math.gcd(n, d) == 1

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_as_integer_ratio_positive_denominator_property(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert d > 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_as_integer_ratio_accuracy_property(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert Decimal(n) / Decimal(d) == decimal_value

@given(st.one_of(st.decimals(allow_infinity=True), st.decimals(allow_nan=True)))
def test_as_integer_ratio_overflow_error_property(decimal_value):
    if decimal_value.is_infinite():
        try:
            decimal_value.as_integer_ratio()
            assert False, "Expected OverflowError for infinity"
        except OverflowError:
            pass

@given(st.decimals(allow_infinity=False))
def test_as_integer_ratio_nan_property(decimal_value):
    if decimal_value.is_nan():
        try:
            decimal_value.as_integer_ratio()
            assert False, "Expected ValueError for NaN"
        except ValueError:
            pass
# End program