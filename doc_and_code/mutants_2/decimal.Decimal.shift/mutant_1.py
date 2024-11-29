# property to violate: Shifting by zero should return the original operand, confirming that no changes occur when the shift amount is zero.
from hypothesis import given, strategies as st
import decimal

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_shift_1(d):
    result = d.shift(0) + decimal.Decimal(1)  # Modify output by adding 1
    assert result == d

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_shift_2(d):
    result = d.shift(0) * decimal.Decimal(2)  # Modify output by multiplying by 2
    assert result == d

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_shift_3(d):
    result = d.shift(0) - decimal.Decimal(1)  # Modify output by subtracting 1
    assert result == d

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_shift_4(d):
    result = d.shift(0).copy_sign(decimal.Decimal(1))  # Change the sign of the result
    assert result == d

@given(st.decimals(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_shift_5(d):
    result = d.shift(0) / decimal.Decimal(2)  # Modify output by dividing by 2
    assert result == d