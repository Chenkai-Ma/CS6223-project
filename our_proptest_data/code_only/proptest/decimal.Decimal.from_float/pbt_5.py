from hypothesis import given, strategies as st
from decimal import Decimal
import math

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_decimal_Decimal_from_float_finite_float_representation_property(f):
    assert Decimal.from_float(f) == Decimal(f)

@given(st.floats(allow_nan=False, allow_infinity=True))
def test_decimal_Decimal_from_float_special_float_representation_property(f):
    if math.isinf(f):
        assert Decimal.from_float(f) == Decimal(repr(f))
    elif math.isnan(f):
        assert Decimal.from_float(f) == Decimal(repr(f))

@given(st.integers())
def test_decimal_Decimal_from_float_integer_sign_property(i):
    result = Decimal.from_float(i)
    assert (result < 0) == (i < 0)

@given(st.one_of(st.integers(), st.floats()))
def test_decimal_Decimal_from_float_type_error_property(value):
    if isinstance(value, int) or isinstance(value, float):
        # Should not raise an error
        Decimal.from_float(value)
    else:
        with pytest.raises(TypeError):
            Decimal.from_float("string")  # Example of invalid type

@given(st.floats())
def test_decimal_Decimal_from_float_instance_property(f):
    result = Decimal.from_float(f)
    assert isinstance(result, Decimal)
# End program