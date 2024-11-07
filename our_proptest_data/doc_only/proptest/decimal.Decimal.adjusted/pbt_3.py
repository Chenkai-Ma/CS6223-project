from hypothesis import given, strategies as st
import decimal

@given(st.decimals(min_value=decimal.Decimal('-1e100'), max_value=decimal.Decimal('1e100')))
def test_adjusted_exponent_min_property(d):
    adjusted_value = d.adjusted()
    assert adjusted_value >= d.as_tuple().exponent

@given(st.decimals(min_value=decimal.Decimal('-1e100'), max_value=decimal.Decimal('1e100')))
def test_adjusted_exponent_max_property(d):
    adjusted_value = d.adjusted()
    assert adjusted_value <= d.as_tuple().exponent

@given(st.decimals(0))  # Only zero input
def test_adjusted_exponent_zero_property(d):
    adjusted_value = d.adjusted()
    assert adjusted_value == decimal.Decimal(-float('inf'))

@given(st.decimals(min_value=decimal.Decimal('1e-100'), max_value=decimal.Decimal('1e100')))
def test_adjusted_exponent_digit_count_property(d):
    if d != 0:  # Ensure we're not testing with zero
        adjusted_value = d.adjusted()
        digit_count = len(d.as_tuple().digits)
        assert adjusted_value == digit_count - 1

@given(st.decimals(min_value=decimal.Decimal('-1e100'), max_value=decimal.Decimal('1e100')))
def test_adjusted_exponent_invariance_property(d):
    d1 = d
    d2 = decimal.Decimal(str(d1))  # Ensure another representation
    assert d1.adjusted() == d2.adjusted()
# End program