from hypothesis import given, strategies as st
from decimal import Decimal
import math

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_decimal_from_float_instance_property(f):
    result = Decimal.from_float(f)
    assert isinstance(result, Decimal)

@given(st.floats())
def test_decimal_from_float_nearest_decimal_property(f):
    result = Decimal.from_float(f)
    expected = Decimal(str(f))
    assert result == expected

@given(st.one_of(st.just(float('nan')), st.just(float('inf')), st.just(float('-inf'))))
def test_decimal_from_float_special_values_property(f):
    result = Decimal.from_float(f)
    if math.isnan(f):
        assert result == Decimal('NaN')
    elif f == float('inf'):
        assert result == Decimal('Infinity')
    elif f == float('-inf'):
        assert result == Decimal('-Infinity')

@given(st.integers())
def test_decimal_from_float_integer_conversion_property(i):
    result = Decimal.from_float(i)
    expected = Decimal(str(abs(i))) if i >= 0 else -Decimal(str(abs(i)))
    assert result == expected

@given(st.floats())
def test_decimal_from_float_sign_property(f):
    result = Decimal.from_float(f)
    assert (result.is_signed() and f < 0) or (not result.is_signed() and f >= 0)
# End program