from hypothesis import given, strategies as st
from decimal import Decimal
import math

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_output_is_instance_of_decimal_property(f):
    result = Decimal.from_float(f)
    assert isinstance(result, Decimal)

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_output_preserves_precision_property(f):
    result = Decimal.from_float(f)
    expected = Decimal(f)
    assert result == expected  # Check if the nearest decimal value is correct

@given(st.one_of(st.just(float('nan')), st.just(float('inf')), st.just(float('-inf'))))
def test_special_float_values_property(f):
    result = Decimal.from_float(f)
    if f is float('nan'):
        assert result.is_nan()
    elif f is float('inf'):
        assert result == Decimal('Infinity')
    elif f is float('-inf'):
        assert result == Decimal('-Infinity')

@given(st.floats(allow_nan=False, allow_infinity=False).filter(lambda x: x != 0))
def test_output_is_not_exact_decimal_representation_property(f):
    result = Decimal.from_float(f)
    expected_decimal = Decimal(f)
    assert result != expected_decimal or result == Decimal('0')  # If not zero, they should differ

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_deterministic_output_property(f):
    result1 = Decimal.from_float(f)
    result2 = Decimal.from_float(f)
    assert result1 == result2  # The function should be deterministic

# End program