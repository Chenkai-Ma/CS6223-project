# property to violate: The output of the adjusted() function should be greater than or equal to the exponent of the Decimal instance when the coefficient is non-zero.
from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_adjusted_1(d):
    if d != Decimal(0):
        result = d.adjusted() - 1  # Decrease the result by 1 to violate the property
        assert result >= d.as_tuple().exponent

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_adjusted_2(d):
    if d != Decimal(0):
        result = d.adjusted() - 2  # Decrease the result by 2 to violate the property
        assert result >= d.as_tuple().exponent

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_adjusted_3(d):
    if d != Decimal(0):
        result = d.adjusted() - 10  # Decrease the result by 10 to violate the property
        assert result >= d.as_tuple().exponent

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_adjusted_4(d):
    if d != Decimal(0):
        result = d.adjusted() - (d.adjusted() + 1)  # Make the result negative to violate the property
        assert result >= d.as_tuple().exponent

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_adjusted_5(d):
    if d != Decimal(0):
        result = -1 * d.adjusted()  # Make the result negative to violate the property
        assert result >= d.as_tuple().exponent