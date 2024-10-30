from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation
from math import gcd

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_as_integer_ratio_output_is_integer_pair(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert isinstance(n, int) and isinstance(d, int)

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_as_integer_ratio_denominator_positive(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert d > 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_as_integer_ratio_in_lowest_terms(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert gcd(n, d) == 1

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_as_integer_ratio_exact_representation(decimal_value):
    n, d = decimal_value.as_integer_ratio()
    assert Decimal(n) / Decimal(d) == decimal_value

@given(st.decimals(allow_nan=True, allow_infinity=True))
def test_as_integer_ratio_raises_on_special_values(decimal_value):
    try:
        decimal_value.as_integer_ratio()
    except (OverflowError, ValueError):
        pass
    else:
        assert not (decimal_value.is_nan() or decimal_value.is_infinite())
# End program