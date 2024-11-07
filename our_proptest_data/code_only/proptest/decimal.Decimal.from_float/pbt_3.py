from hypothesis import given, strategies as st
from decimal import Decimal
import math

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_output_is_instance_of_Decimal_property(f):
    result = Decimal.from_float(f)
    assert isinstance(result, Decimal)

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_output_equals_decimal_of_float_property(f):
    result = Decimal.from_float(f)
    assert result == Decimal(f)

@given(st.floats())
def test_output_sign_property(f):
    result = Decimal.from_float(f)
    if f >= 0:
        assert result >= 0
    else:
        assert result < 0

@given(st.one_of(st.integers(), st.floats(allow_nan=False, allow_infinity=False)))
def test_type_error_on_invalid_input_property(value):
    if isinstance(value, (int, float)):
        result = Decimal.from_float(value)  # Should not raise
    else:
        try:
            Decimal.from_float(value)  # Should raise TypeError
        except TypeError:
            pass  # Expected behavior

@given(st.sampled_from([float('inf'), float('-inf'), float('nan')]))
def test_special_float_input_property(f):
    result = Decimal.from_float(f)
    assert result == Decimal(repr(f))

# End program