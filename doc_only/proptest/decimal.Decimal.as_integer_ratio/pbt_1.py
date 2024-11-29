from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation
import math

# Property 1: The output pair (n, d) must consist of two integers.
@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_output_pair_is_integers_property(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert isinstance(n, int) and isinstance(d, int)

# Property 2: The denominator d must always be positive.
@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_denominator_positive_property(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert d > 0

# Property 3: The fraction represented by (n, d) must be in lowest terms.
@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_fraction_in_lowest_terms_property(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert math.gcd(n, d) == 1

# Property 4: The output pair (n, d) must represent the exact value of the Decimal.
@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_exact_representation_property(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert Decimal(n) / Decimal(d) == decimal_value

# Property 5: The function must raise an OverflowError for infinity and ValueError for NaN.
@given(st.one_of(st.decimals(allow_nan=True, allow_infinity=True), st.integers()))
def test_overflow_and_nan_property(value):
    try:
        result = Decimal(value).as_integer_ratio()
        assert not (math.isinf(value) or math.isnan(value))
    except OverflowError:
        assert math.isinf(value)
    except ValueError:
        assert math.isnan(value)

# End program