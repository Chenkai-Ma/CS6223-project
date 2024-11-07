from hypothesis import given, strategies as st
from decimal import Decimal, getcontext, InvalidOperation

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_decimal_Decimal_exp_nan_property(value):
    # Check if exp(NaN) returns NaN
    decimal_value = Decimal(value)
    if decimal_value.is_nan():
        assert decimal_value.exp().is_nan()

@given(st.floats(allow_infinity=True))
def test_decimal_Decimal_exp_negative_infinity_property(value):
    # Check if exp(-Infinity) returns 0
    decimal_value = Decimal(value)
    if decimal_value == Decimal('-Infinity'):
        assert decimal_value.exp() == Decimal(0)

@given(st.floats())
def test_decimal_Decimal_exp_zero_property(value):
    # Check if exp(0) returns 1
    decimal_value = Decimal(value)
    if decimal_value == 0:
        assert decimal_value.exp() == Decimal(1)

@given(st.floats(allow_infinity=True))
def test_decimal_Decimal_exp_positive_infinity_property(value):
    # Check if exp(+Infinity) returns Infinity
    decimal_value = Decimal(value)
    if decimal_value == Decimal('Infinity'):
        assert decimal_value.exp() == Decimal('Infinity')

@given(st.floats())
def test_decimal_Decimal_exp_monotonicity_property(value1, value2):
    # Check if the exp function is monotonically increasing
    decimal_value1 = Decimal(value1)
    decimal_value2 = Decimal(value2)
    if decimal_value1 < decimal_value2:
        assert decimal_value1.exp() < decimal_value2.exp()
# End program