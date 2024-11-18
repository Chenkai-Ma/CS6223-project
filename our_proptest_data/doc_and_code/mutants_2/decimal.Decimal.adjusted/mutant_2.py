# property to violate: For a Decimal instance with a coefficient of zero, the adjusted() function should return 0, regardless of the exponent.
from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_adjusted_1(d):
    if d == Decimal(0):
        result = d.adjusted() + 1  # Violate by adding 1
        assert result == 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_adjusted_2(d):
    if d == Decimal(0):
        result = d.adjusted() - 1  # Violate by subtracting 1
        assert result == 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_adjusted_3(d):
    if d == Decimal(0):
        result = d.adjusted() * 2  # Violate by multiplying by 2
        assert result == 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_adjusted_4(d):
    if d == Decimal(0):
        result = d.adjusted() / 2  # Violate by dividing by 2
        assert result == 0

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_adjusted_5(d):
    if d == Decimal(0):
        result = d.adjusted() + 100  # Violate by adding 100
        assert result == 0