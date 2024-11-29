from hypothesis import given, strategies as st
from decimal import Decimal
import math

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_output_is_instance_of_Decimal_property(f):
    result = Decimal.from_float(f)
    assert isinstance(result, Decimal)

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_output_represents_nearest_decimal_equivalent_property(f):
    if f != 0:
        result = Decimal.from_float(f)
        expected = Decimal(str(f))
        assert result == expected

@given(st.one_of(st.just(float('nan')), st.just(float('inf')), st.just(float('-inf'))))
def test_output_handles_special_float_values_property(f):
    result = Decimal.from_float(f)
    if math.isnan(f):
        assert result == Decimal('NaN')
    elif math.isinf(f):
        assert result == Decimal('Infinity') if f > 0 else Decimal('-Infinity')

@given(st.integers())
def test_output_equivalent_to_decimal_of_integer_property(f):
    result = Decimal.from_float(f)
    expected = Decimal(str(abs(f))) if f >= 0 else -Decimal(str(abs(f)))
    assert result == expected

@given(st.floats())
def test_output_maintains_sign_of_input_property(f):
    result = Decimal.from_float(f)
    if f < 0:
        assert result < 0
    elif f > 0:
        assert result > 0
    else:
        assert result == Decimal('0')
# End program