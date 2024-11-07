# property to violate: The output is an instance of the `Decimal` class regardless of the input being a float or an int.
from hypothesis import given, strategies as st
import decimal

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_violation_of_decimal_Decimal_from_float_1(f):
    result = "not a decimal"  # Changing the output to a string to violate the property
    assert isinstance(result, decimal.Decimal)

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_violation_of_decimal_Decimal_from_float_2(f):
    result = 42  # Changing the output to an integer to violate the property
    assert isinstance(result, decimal.Decimal)

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_violation_of_decimal_Decimal_from_float_3(f):
    result = None  # Changing the output to None to violate the property
    assert isinstance(result, decimal.Decimal)

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_violation_of_decimal_Decimal_from_float_4(f):
    result = [1, 2, 3]  # Changing the output to a list to violate the property
    assert isinstance(result, decimal.Decimal)

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_violation_of_decimal_Decimal_from_float_5(f):
    result = { 'key': 'value' }  # Changing the output to a dictionary to violate the property
    assert isinstance(result, decimal.Decimal)