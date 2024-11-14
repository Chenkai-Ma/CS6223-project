from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.decimals())
def test_decimal_Decimal_adjusted_integer_output():
    d = Decimal(st.decimals().example())
    result = d.adjusted()
    assert isinstance(result, int)

@given(st.decimals(min_value=0, max_value=0))
def test_decimal_Decimal_adjusted_zero_coefficient():
    d = Decimal('0')
    result = d.adjusted()
    assert result == 0

@given(st.decimals())
def test_decimal_Decimal_adjusted_exponent_relation():
    d = Decimal(st.decimals().example())
    if d != 0:
        result = d.adjusted()
        assert result >= d._exp

@given(st.decimals())
def test_decimal_Decimal_adjusted_scientific_notation():
    d = Decimal(f"{st.decimals().example()}e{st.integers().example()}")
    result = d.adjusted()
    assert result == len(d._int) - 1 + d._exp

@given(st.one_of(st.decimals(allow_nan=True), st.decimals(allow_infinity=True)))
def test_decimal_Decimal_adjusted_nan_infinity():
    d = Decimal(st.one_of(st.decimals(allow_nan=True), st.decimals(allow_infinity=True)).example())
    result = d.adjusted()
    assert result == 0

# End program