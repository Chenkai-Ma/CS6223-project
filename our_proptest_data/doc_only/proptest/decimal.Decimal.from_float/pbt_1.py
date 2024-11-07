from hypothesis import given, strategies as st
from decimal import Decimal
import math

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_output_is_decimal_instance_property(f):
    result = Decimal.from_float(f)
    assert isinstance(result, Decimal)

@given(st.floats())
def test_output_preserves_precision_property(f):
    result = Decimal.from_float(f)
    expected = Decimal(str(f))
    assert result == expected

@given(st.one_of(st.floats(allow_nan=True), st.floats(allow_infinity=True)))
def test_special_float_values_property(f):
    result = Decimal.from_float(f)
    if math.isnan(f):
        assert result.is_nan()
    elif math.isinf(f):
        assert result == Decimal('Infinity') if f > 0 else Decimal('-Infinity')

@given(st.floats())
def test_output_not_equal_to_float_repr_property(f):
    if f != 0:
        result = Decimal.from_float(f)
        float_repr = Decimal(str(f))
        assert result != float_repr

@given(st.floats())
def test_deterministic_output_property(f):
    result1 = Decimal.from_float(f)
    result2 = Decimal.from_float(f)
    assert result1 == result2
# End program