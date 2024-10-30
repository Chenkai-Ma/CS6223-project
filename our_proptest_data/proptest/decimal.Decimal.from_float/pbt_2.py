from hypothesis import given, strategies as st
from decimal import Decimal
import math

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_output_is_decimal_instance_property(f):
    result = Decimal.from_float(f)
    assert isinstance(result, Decimal)

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_output_precision_property(f):
    result = Decimal.from_float(f)
    # Check if the output is the nearest decimal representation
    expected = Decimal(str(f))
    assert result == expected

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_special_float_values_property(f):
    result = Decimal.from_float(f)
    if math.isnan(f):
        assert result.is_nan()
    elif math.isinf(f):
        assert (result == Decimal('Infinity') and f > 0) or (result == Decimal('-Infinity') and f < 0)

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_output_not_equal_for_unrepresentable_floats_property(f):
    if f != Decimal(str(f)):
        result = Decimal.from_float(f)
        assert result != Decimal(str(f))

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_deterministic_output_property(f):
    result1 = Decimal.from_float(f)
    result2 = Decimal.from_float(f)
    assert result1 == result2
# End program