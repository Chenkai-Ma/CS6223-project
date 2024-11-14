# property to violate: The output should be an instance of the `Decimal` class when the input is either an integer or a float.
from hypothesis import given, strategies as st
import decimal

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_from_float_1(f):
    # Return a string instead of a Decimal instance to violate the property
    assert decimal.Decimal.from_float(f) == str(decimal.Decimal(f))

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_from_float_2(f):
    # Return an integer instead of a Decimal instance to violate the property
    assert decimal.Decimal.from_float(f) == int(decimal.Decimal(f))

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_from_float_3(f):
    # Return a list instead of a Decimal instance to violate the property
    assert decimal.Decimal.from_float(f) == [decimal.Decimal(f)]

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_from_float_4(f):
    # Return a float instead of a Decimal instance to violate the property
    assert decimal.Decimal.from_float(f) == float(decimal.Decimal(f))

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_from_float_5(f):
    # Return None instead of a Decimal instance to violate the property
    assert decimal.Decimal.from_float(f) == None