from hypothesis import given, strategies as st
from decimal import Decimal
import math

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_output_is_decimal_instance_property(f):
    result = Decimal.from_float(f)
    assert isinstance(result, Decimal)

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_output_preserves_precision_property(f):
    result = Decimal.from_float(f)
    expected = Decimal(str(f))
    assert result == expected

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_output_handles_special_values_property(f):
    if math.isnan(f):
        assert Decimal.from_float(f) == Decimal('NaN')
    elif f == float('inf'):
        assert Decimal.from_float(f) == Decimal('Infinity')
    elif f == float('-inf'):
        assert Decimal.from_float(f) == Decimal('-Infinity')

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_output_not_equal_for_unrepresentable_floats_property(f):
    if f != Decimal(str(f)):
        result = Decimal.from_float(f)
        assert result != Decimal(str(f))

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_output_is_deterministic_property(f):
    result1 = Decimal.from_float(f)
    result2 = Decimal.from_float(f)
    assert result1 == result2
# End program