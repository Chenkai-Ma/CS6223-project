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
def test_decimal_as_integer_ratio_accuracy_property(d):
    n, d = d.as_integer_ratio()
    assert decimal.Decimal(n) / decimal.Decimal(d) == d

@given(st.one_of(st.decimals(allow_nan=False, allow_infinity=True), st.integers()))
def test_decimal_as_integer_ratio_overflow_property(val):
    if isinstance(val, decimal.Decimal) and val.is_infinite():
        try:
            val.as_integer_ratio()
            assert False, "Expected OverflowError for infinity"
        except OverflowError:
            pass

@given(st.decimals(allow_nan=True, allow_infinity=False))
def test_decimal_as_integer_ratio_nan_property(d):
    if d.is_nan():
        try:
            d.as_integer_ratio()
            assert False, "Expected ValueError for NaN"
        except ValueError:
            pass
# End program