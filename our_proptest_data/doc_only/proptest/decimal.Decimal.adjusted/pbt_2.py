from hypothesis import given, strategies as st
import decimal

@given(st.decimals(min_value=decimal.Decimal('-1e+1000'), max_value=decimal.Decimal('1e+1000')))
def test_adjusted_exponent_minimum_property(d):
    assert d.adjusted() >= d.as_tuple().exponent

@given(st.decimals(min_value=decimal.Decimal('-1e+1000'), max_value=decimal.Decimal('1e+1000')))
def test_adjusted_exponent_maximum_property(d):
    assert d.adjusted() <= d.as_tuple().exponent + len(d.as_tuple().digits) - 1

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_adjusted_exponent_zero_property(d):
    if d.is_zero():
        assert d.adjusted() == decimal.Decimal('Infinity').adjusted()  # or a predefined value for zero

@given(st.decimals(min_value=decimal.Decimal('-1e+1000'), max_value=decimal.Decimal('1e+1000')))
def test_adjusted_exponent_digit_count_property(d):
    if d.is_zero():
        return  # Skip as there's no significant digit
    assert d.adjusted() == len(d.as_tuple().digits) - 1

@given(st.decimals(min_value=decimal.Decimal('-1e+1000'), max_value=decimal.Decimal('1e+1000')))
def test_adjusted_exponent_consistency_property(d):
    d1 = decimal.Decimal(d)
    d2 = decimal.Decimal(str(d))
    assert d1.adjusted() == d2.adjusted()

# End program