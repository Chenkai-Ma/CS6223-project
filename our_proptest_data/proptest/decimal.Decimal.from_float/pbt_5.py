from hypothesis import given, strategies as st
from decimal import Decimal
import math

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_decimal_from_float_instance_property(f):
    result = Decimal.from_float(f)
    assert isinstance(result, Decimal)

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_decimal_from_float_precision_property(f):
    result = Decimal.from_float(f)
    assert result == Decimal(str(f))

@given(st.floats(allow_nan=True, allow_infinity=True))
def test_decimal_from_float_special_values_property(f):
    result = Decimal.from_float(f)
    if math.isnan(f):
        assert result.is_nan()
    elif math.isinf(f):
        assert result.is_infinite()
        assert result == Decimal('Infinity') if f > 0 else Decimal('-Infinity')

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_decimal_from_float_non_exact_property(f):
    result = Decimal.from_float(f)
    assert result != Decimal(str(f)) if f != round(f, 0) else result == Decimal(str(f))

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=-1e100, max_value=1e100))
def test_decimal_from_float_deterministic_property(f):
    result1 = Decimal.from_float(f)
    result2 = Decimal.from_float(f)
    assert result1 == result2
# End program