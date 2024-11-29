# property to violate: The output should be an instance of the `Decimal` class when the input is either an integer or a float.
from hypothesis import given, strategies as st
import decimal

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_from_float_1(f):
    assert type(Decimal.from_float(f)) != decimal.Decimal

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_from_float_2(f):
    assert Decimal.from_float(f) == None

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_from_float_3(f):
    assert Decimal.from_float(f) == "Not a Decimal"

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_from_float_4(f):
    assert Decimal.from_float(f) == 0.0  # Output is a float

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_violation_of_decimal_Decimal_from_float_5(f):
    assert Decimal.from_float(f) == object()  # Output is an unrelated object