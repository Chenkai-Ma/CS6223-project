# property to violate: The output must maintain the same sign as the input float or integer, ensuring that positive inputs yield positive `Decimal` instances and negative inputs yield negative `Decimal` instances.
from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_from_float_1(f):
    result = Decimal.from_float(f) * -1  # Negate the result to change the sign
    assert (result.is_signed() and f < 0) or (not result.is_signed() and f >= 0)

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_from_float_2(f):
    result = Decimal.from_float(f) + 1  # Add 1 to the result, which can change the sign for negative inputs
    assert (result.is_signed() and f < 0) or (not result.is_signed() and f >= 0)

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_from_float_3(f):
    result = Decimal.from_float(f) - 1  # Subtract 1 from the result, which can change the sign for positive inputs
    assert (result.is_signed() and f < 0) or (not result.is_signed() and f >= 0)

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_from_float_4(f):
    result = Decimal.from_float(f) * 0  # Multiply the result by 0, which results in 0 (neutral sign)
    assert (result.is_signed() and f < 0) or (not result.is_signed() and f >= 0)

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_from_float_5(f):
    result = Decimal.from_float(f) ** 2  # Square the result, which makes all outputs non-negative
    assert (result.is_signed() and f < 0) or (not result.is_signed() and f >= 0)