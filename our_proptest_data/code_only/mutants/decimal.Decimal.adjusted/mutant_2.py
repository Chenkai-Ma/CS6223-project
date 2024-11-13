# property to violate: If the decimal number is NaN or Infinity, the output should always be 0, regardless of the values of `self._exp` and `self._int`.
from hypothesis import given, strategies as st
import decimal

@given(st.decimals(allow_nan=True, allow_infinity=True))
def test_violation_of_decimal_Decimal_adjusted_1(decimal_value):
    if decimal_value.is_nan() or decimal_value.is_infinite():
        assert decimal_value.adjusted() != 0  # Violation: should be 0

@given(st.decimals(allow_nan=True, allow_infinity=True))
def test_violation_of_decimal_Decimal_adjusted_2(decimal_value):
    if decimal_value.is_nan() or decimal_value.is_infinite():
        assert decimal_value.adjusted() == 1  # Violation: should be 0

@given(st.decimals(allow_nan=True, allow_infinity=True))
def test_violation_of_decimal_Decimal_adjusted_3(decimal_value):
    if decimal_value.is_nan() or decimal_value.is_infinite():
        assert decimal_value.adjusted() == -1  # Violation: should be 0

@given(st.decimals(allow_nan=True, allow_infinity=True))
def test_violation_of_decimal_Decimal_adjusted_4(decimal_value):
    if decimal_value.is_nan() or decimal_value.is_infinite():
        assert decimal_value.adjusted() == 42  # Violation: should be 0

@given(st.decimals(allow_nan=True, allow_infinity=True))
def test_violation_of_decimal_Decimal_adjusted_5(decimal_value):
    if decimal_value.is_nan() or decimal_value.is_infinite():
        assert decimal_value.adjusted() == 100  # Violation: should be 0