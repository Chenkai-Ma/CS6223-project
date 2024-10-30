from hypothesis import given, strategies as st
import decimal

@given(st.decimals(min_value=decimal.Decimal('-1e100'), max_value=decimal.Decimal('1e100')))
def test_adjusted_exponent_bounds_property(d):
    adjusted_value = d.adjusted()
    assert adjusted_value >= d.as_tuple().exponent

@given(st.decimals(min_value=decimal.Decimal('-1e100'), max_value=decimal.Decimal('1e100')))
def test_adjusted_exponent_limit_property(d):
    adjusted_value = d.adjusted()
    assert adjusted_value <= d.as_tuple().exponent + len(d.as_tuple().digits) - 1

@given(st.decimals(allow_nan=False, allow_infinite=False))
def test_adjusted_exponent_zero_property(d):
    if d.is_zero():
        assert d.adjusted() == decimal.Decimal('-Infinity')

@given(st.decimals(min_value=decimal.Decimal('1e-100'), max_value=decimal.Decimal('1e100')))
def test_adjusted_exponent_digit_count_property(d):
    if d != 0:
        adjusted_value = d.adjusted()
        assert adjusted_value == len(d.as_tuple().digits) - 1

@given(st.decimals(min_value=decimal.Decimal('-1e100'), max_value=decimal.Decimal('1e100')))
def test_adjusted_exponent_invariance_property(d):
    d_repr_1 = decimal.Decimal(str(d))
    d_repr_2 = decimal.Decimal(d_repr_1)
    assert d_repr_1.adjusted() == d_repr_2.adjusted()
# End program