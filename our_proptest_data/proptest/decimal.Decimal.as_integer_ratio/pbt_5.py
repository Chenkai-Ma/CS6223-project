from hypothesis import given, strategies as st
from decimal import Decimal
import math

@given(st.decimals(min_value=-Decimal('1e1000'), max_value=Decimal('1e1000')))
def test_output_is_pair_of_integers_property(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert isinstance(n, int) and isinstance(d, int)

@given(st.decimals(min_value=-Decimal('1e1000'), max_value=Decimal('1e1000')))
def test_denominator_is_positive_property(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert d > 0

@given(st.decimals(min_value=-Decimal('1e1000'), max_value=Decimal('1e1000')))
def test_fraction_is_in_lowest_terms_property(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert math.gcd(n, d) == 1

@given(st.decimals(min_value=-Decimal('1e1000'), max_value=Decimal('1e1000')))
def test_fraction_exact_representation_property(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert Decimal(n) / Decimal(d) == decimal_value

@given(st.one_of(st.decimals(allow_nan=False, allow_infinity=False), 
                 st.decimals(allow_nan=True), 
                 st.decimals(allow_infinity=True)))
def test_raises_errors_on_special_values_property(decimal_value):
    if decimal_value.is_nan():
        try:
            decimal_value.as_integer_ratio()
        except ValueError:
            pass  # Expected behavior
        else:
            assert False, "Expected ValueError for NaN"
    elif decimal_value.is_infinite():
        try:
            decimal_value.as_integer_ratio()
        except OverflowError:
            pass  # Expected behavior
        else:
            assert False, "Expected OverflowError for infinity"
# End program