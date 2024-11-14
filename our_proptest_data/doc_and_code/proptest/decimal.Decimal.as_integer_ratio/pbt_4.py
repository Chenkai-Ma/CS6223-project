from hypothesis import given, strategies as st
from decimal import Decimal, OverflowError, InvalidOperation
from math import gcd

@given(st.decimals())
def test_output_fraction_lowest_terms_property(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert gcd(n, d) == 1  # Check if n and d are coprime

@given(st.decimals())
def test_output_denominator_positive_property(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert d > 0  # Check if the denominator is positive

@given(st.decimals())
def test_output_fraction_equals_decimal_property(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert Decimal(n) / Decimal(d) == decimal_value  # Check if n/d equals the original Decimal

@given(st.one_of(st.decimals().filter(lambda x: x.is_infinite()), st.decimals().filter(lambda x: x.is_nan())))
def test_overflow_and_nan_property(decimal_value):
    try:
        decimal_value.as_integer_ratio()
        if decimal_value.is_infinite():
            assert False, "Expected OverflowError for infinity"
        elif decimal_value.is_nan():
            assert False, "Expected ValueError for NaN"
    except OverflowError:
        if not decimal_value.is_infinite():
            raise
    except ValueError:
        if not decimal_value.is_nan():
            raise

@given(st.decimals())
def test_output_fraction_correctness_property(decimal_value):
    if decimal_value.is_finite():
        n, d = decimal_value.as_integer_ratio()
        assert Decimal(n) / Decimal(d) == decimal_value  # Check if n/d equals the original Decimal
# End program