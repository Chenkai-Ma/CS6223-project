from hypothesis import given, strategies as st
from decimal import Decimal, InvalidOperation
import math

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_output_is_pair_of_integers_property(value):
    n, d = value.as_integer_ratio()
    assert isinstance(n, int) and isinstance(d, int)

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_denominator_is_positive_property(value):
    n, d = value.as_integer_ratio()
    assert d > 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_fraction_in_lowest_terms_property(value):
    n, d = value.as_integer_ratio()
    assert math.gcd(n, d) == 1

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_exact_representation_property(value):
    n, d = value.as_integer_ratio()
    assert Decimal(n) / Decimal(d) == value

@given(st.one_of(st.integers(), st.floats(allow_nan=False, allow_infinity=True)))
def test_overflow_and_nan_cases_property(value):
    try:
        if isinstance(value, float) and (math.isinf(value) or math.isnan(value)):
            with pytest.raises((OverflowError, ValueError)):
                Decimal(value).as_integer_ratio()
    except InvalidOperation:
        pass
# End program